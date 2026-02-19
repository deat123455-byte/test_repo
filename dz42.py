import telebot
import os
from datetime import datetime
from dotenv import load_dotenv
import sqlite3
from contextlib import contextmanager

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

# Путь к базе данных
DB_PATH = 'sleep_bot.db'

# Контекстный менеджер для работы с базой данных
@contextmanager
def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Чтобы можно было обращаться к колонкам по имени
    try:
        yield conn
    finally:
        conn.close()

# Инициализация базы данных
def init_db():
    with get_db_connection() as conn:
        # Создание таблицы пользователей
        conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT
            )
        ''')

        # Создание таблицы записей о сне
        conn.execute('''
            CREATE TABLE IF NOT EXISTS sleep_records (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                sleep_time DATETIME,
                wake_time DATETIME,
                sleep_quality INTEGER,
                FOREIGN KEY (user_id) REFERENCES users (id)
            )
        ''')

        # Создание таблицы заметок
        conn.execute('''
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT,
                sleep_record_id INTEGER,
                FOREIGN KEY (sleep_record_id) REFERENCES sleep_records (id)
            )
        ''')

        conn.commit()

# Функции для работы с базой данных

# Работа с пользователями
def get_or_create_user(user_id: int, username: str = None):
    """Получить пользователя или создать нового"""
    with get_db_connection() as conn:
        # Проверяем, существует ли пользователь
        user = conn.execute(
            'SELECT * FROM users WHERE id = ?', 
            (user_id,)
        ).fetchone()
        
        if not user:
            # Создаем нового пользователя
            conn.execute(
                'INSERT OR IGNORE INTO users (id, name) VALUES (?, ?)',
                (user_id, username if username else f"User_{user_id}")
            )
            conn.commit()
            return True
        return False

# Работа с записями о сне
def save_sleep_record(user_id: int, sleep_time: datetime, wake_time: datetime, sleep_quality: int = None):
    """Сохранить запись о сне"""
    with get_db_connection() as conn:
        conn.execute('''
            INSERT INTO sleep_records (user_id, sleep_time, wake_time, sleep_quality)
            VALUES (?, ?, ?, ?)
        ''', (user_id, sleep_time, wake_time, sleep_quality))
        conn.commit()
        return conn.lastrowid

def save_note(sleep_record_id: int, text: str):
    """Сохранить заметку к записи о сне"""
    with get_db_connection() as conn:
        conn.execute('''
            INSERT INTO notes (sleep_record_id, text)
            VALUES (?, ?)
        ''', (sleep_record_id, text))
        conn.commit()

def get_user_sleep_records(user_id: int):
    """Получить все записи о сне пользователя"""
    with get_db_connection() as conn:
        records = conn.execute('''
            SELECT * FROM sleep_records WHERE user_id = ?
            ORDER BY sleep_time DESC
        ''', (user_id,)).fetchall()
        return [dict(record) for record in records]

def get_latest_sleep_record(user_id: int):
    """Получить последнюю запись о сне пользователя"""
    with get_db_connection() as conn:
        record = conn.execute('''
            SELECT * FROM sleep_records
            WHERE user_id = ?
            ORDER BY sleep_time DESC
            LIMIT 1
        ''', (user_id,)).fetchone()
        return dict(record) if record else None

# Переменные для хранения состояний (для совместимости с текущей логикой)
last_sleep_time = {}
states = {}
pending_record_id = {}  # Для хранения ID записи при ожидании заметки

@bot.message_handler(commands=['start'])
def start(message):
    # Создаем пользователя если он еще не существует
    get_or_create_user(message.from_user.id, message.from_user.username)
    bot.send_message(message.chat.id, 'Привет! Я буду помогать отслеживать параметры сна. Используй команды /sleep, /wake, /quality и /notes.')

@bot.message_handler(commands=['sleep'])
def sleep_command(message):
    chat_id = message.chat.id
    current_time = datetime.now()
    last_sleep_time[chat_id] = current_time
    bot.send_message(chat_id, 'Спокойной ночи, не забудь мне сообщить, когда проснешься командой /wake.')

@bot.message_handler(commands=['wake'])
def wake_command(message):
    chat_id = message.chat.id
    if chat_id in last_sleep_time:
        sleep_time = last_sleep_time[chat_id]
        wake_time = datetime.now()
        time_difference = wake_time - sleep_time
        duration = time_difference.total_seconds()
        minutes, seconds = divmod(duration, 60)
        hours, minutes = divmod(minutes, 60)

        formatted_difference = f"{int(hours)} часов, {int(minutes)} минут, {int(seconds)} секунд"
        bot.send_message(chat_id, f'Доброе утро! Ты проспал около {formatted_difference}. Не забудь оценить качество сна командой /quality и оставить заметки командой /notes.')

        # Сохраняем запись о сне в базу данных
        record_id = save_sleep_record(
            user_id=chat_id,
            sleep_time=sleep_time,
            wake_time=wake_time
        )
        pending_record_id[chat_id] = record_id
    else:
        bot.send_message(chat_id, 'Вы ещё не сообщили, когда ложились спать. Используйте команду /sleep.')

@bot.message_handler(commands=['quality'])
def quality_command(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Поставьте оценку качества сна (1-10):')
    states[chat_id] = 'waiting_for_quality'

@bot.message_handler(commands=['notes'])
def notes_command(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Напишите заметку о сне:')
    states[chat_id] = 'waiting_for_notes'

@bot.message_handler(func=lambda message: states.get(message.chat.id) == 'waiting_for_quality')
def handle_quality(message):
    chat_id = message.chat.id
    try:
        quality = int(message.text)
        if quality < 1 or quality > 10:
            bot.send_message(chat_id, 'Оценка должна быть числом от 1 до 10. Попробуйте снова.')
            return
    except ValueError:
        bot.send_message(chat_id, 'Неверный формат. Введите число от 1 до 10.')
        return

    # Обновляем последнюю запись о сне
    latest_record = get_latest_sleep_record(chat_id)
    if latest_record:
        with get_db_connection() as conn:
            conn.execute('''
                UPDATE sleep_records
                SET sleep_quality = ?
                WHERE id = ?
            ''', (quality, latest_record['id']))
            conn.commit()

    bot.send_message(chat_id, 'Спасибо за оценку качества сна!')
    states[chat_id] = None

@bot.message_handler(func=lambda message: states.get(message.chat.id) == 'waiting_for_notes')
def handle_notes(message):
    chat_id = message.chat.id
    notes = message.text
    # Получаем последнюю запись о сне
    latest_record = get_latest_sleep_record(chat_id)
    record_id = latest_record['id'] if latest_record else pending_record_id.get(chat_id)
    
    if record_id:
        save_note(record_id, notes)

    bot.send_message(chat_id, 'Спасибо за заметку о качестве сна!')
    states[chat_id] = None

# Инициализация базы данных при запуске
init_db()

bot.polling(none_stop=True, interval=0)