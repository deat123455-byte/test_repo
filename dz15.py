from datetime import datetime
import telebot
import random
import os
import glob
from dotenv import load_dotenv

def measure_execution_time(func):
    def wrapper (*args, **kwargs):
        t_start = datetime.now()
        result = func(*args, **kwargs)
        t_finish = datetime.now()
        execution_time = t_finish - t_start
        milliseconds = round(execution_time.microseconds / 1000)
        print(f"Function completed in "
              f"{execution_time.seconds}s {milliseconds}ms")
        return result
    return wrapper

load_dotenv()
bot = telebot.TeleBot(os.getenv('TOKEN'))


image_folder_path = 'mems'

image_files = glob.glob(os.path.join(image_folder_path, '*.jpg'))


@bot.message_handler(commands=['start'])
@measure_execution_time
def start(message):
    print(message)
    bot.send_message(message.chat.id, 'Привет! Я бот, который отправляет мемы. Для получения мема, используй команду /mem')

@bot.message_handler(commands=['mem'])
@measure_execution_time
def mem(message):
    random_image = random.choice(image_files)
    with open(random_image, 'rb') as photo:
        bot.send_photo(message.chat.id, photo)


bot.polling(none_stop=True)