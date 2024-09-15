import asyncio

from telebot import types
from telebot.async_telebot import AsyncTeleBot

from config import settings
from middleware import check_access

bot = AsyncTeleBot(settings.BOT_TOKEN)

@bot.message_handler(commands=['help', 'start'])
@check_access
async def send_welcome(message: types.Message, bot:AsyncTeleBot = bot):
    #print(message.from_user)
    text = 'Hi, I am EchoBot.\nJust write me something and I will repeat it!'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🇷🇺 Русский")
    btn2 = types.KeyboardButton('🇬🇧 English')
    markup.add(btn1, btn2)
    await bot.send_message(message.from_user.id, "🇷🇺 Выберите язык / 🇬🇧 Choose your language", reply_markup=markup)


@bot.message_handler(func=lambda message: True)
@check_access
async def echo_message(message: types.Message, bot:AsyncTeleBot = bot):
    await bot.reply_to(message, message.text)

asyncio.run(bot.polling())