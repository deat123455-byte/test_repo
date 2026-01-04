import telebot
import os
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('BOT_TOKEN')
bot = telebot.TeleBot(os.getenv('BOT_TOKEN'))


user_information = {}
last_message_time = {}
states = {}


def save_data(info):
    with open("user_information.txt", "a", encoding="utf8") as file:
        for chat_id, data in info.items():
            line = f"{chat_id}|{data.get('start_time', 'не указано')}|{data.get('duration', 'не указано')}|{data.get('quality', 'не указано')}|{data.get('notes', 'не указано')}\n"
            file.write(line)

def load_data():
    with open("user_information.txt", "r", encoding="utf8") as file:
        info = file.readlines()
        user_information_id = {}
        for i in info:
            parts = i.split('|')
            chat_id = parts[0]
            start_time = parts[1]
            duration = parts[2]
            quality = parts[3]
            notes = parts[4].strip()
            user_information_id[chat_id] = {
                'start_time': start_time,
                'duration': duration,
                'quality': quality,
                'notes': notes
            }
        return user_information_id


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет! Я буду помогать отслеживать параметры сна. Используй команды /sleep, /wake, /quality и /notes.')


@bot.message_handler(commands=['sleep'])
def sleep_command(message):
    chat_id = message.chat.id
    current_time = datetime.now()
    last_message_time[chat_id] = current_time
    bot.send_message(chat_id, 'Спокойной ночи, не забудь мне сообщить, когда проснешься командой /wake.')


@bot.message_handler(commands=['wake'])
def wake_command(message):
    chat_id = message.chat.id
    if chat_id in last_message_time:
        last_time = last_message_time[chat_id]
        time_difference = datetime.now() - last_time
        duration = time_difference.total_seconds()
        minutes, seconds = divmod(duration, 60)
        hours, minutes = divmod(minutes, 60)

        formatted_difference = f"{int(hours)} часов, {int(minutes)} минут, {int(seconds)} секунд"
        bot.send_message(chat_id, f'Доброе утро! Ты проспал около {formatted_difference}. Не забудь оценить качество сна командой /quality и оставить заметки командой /notes.')
        if chat_id not in user_information:
            user_information[chat_id] = {}
        user_information[chat_id]['start_time'] = last_time
        user_information[chat_id]['duration'] = duration
    else:
        bot.send_message(chat_id, 'Вы ещё не сообщили, когда ложились спать. Используйте команду /sleep.')
    save_data(user_information)


@bot.message_handler(commands=['quality'])
def quality_command(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Поставьте оценку качества сна:')
    states[chat_id] = 'waiting_for_quality'


@bot.message_handler(commands=['notes'])
def notes_command(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Напишите заметку о сне:')
    states[chat_id] = 'waiting_for_notes'


@bot.message_handler(func=lambda message: states.get(message.chat.id) == 'waiting_for_quality')
def handle_quality(message):
    chat_id = message.chat.id
    if chat_id not in user_information:
        user_information[chat_id] = {}
    quality = message.text
    user_information[chat_id]['quality'] = quality
    bot.send_message(chat_id, 'Спасибо за оценку качества сна!')
    states[chat_id] = None
    save_data(user_information)


@bot.message_handler(func=lambda message: states.get(message.chat.id) == 'waiting_for_notes')
def handle_notes(message):
    chat_id = message.chat.id
    if chat_id not in user_information:
        user_information[chat_id] = {}
    notes = message.text
    user_information[chat_id]['notes'] = notes
    bot.send_message(chat_id, 'Спасибо за заметку о качестве сна!')
    states[chat_id] = None
    save_data(user_information)

user_information = load_data()
bot.polling(none_stop=True, interval=0)