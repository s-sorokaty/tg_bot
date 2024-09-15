import telebot
from telebot import types

from config import settings

print(settings.BOT_TOKEN)

bot = telebot.TeleBot(settings.BOT_TOKEN)

@bot.message_handler(commands=['start']) #создаем команду
def start(message):
    markup = types.InlineKeyboardMarkup()
    button1 = types.InlineKeyboardButton("", url='')
    markup.add(button1)
    bot.send_message(message.chat.id, f"Привет, {message.from_user.first_name}! Нажми на кнопку и перейди на сайт)", reply_markup=markup)

bot.polling(none_stop=True)