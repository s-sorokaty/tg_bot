from telebot import types, TeleBot

from config import Settings
from handler import handler
from db.init import init as db_init

settings = Settings()
db_init()
bot = TeleBot(settings.BOT_TOKEN)

@bot.message_handler(commands = ['start'])
def url(message: types.Message):
    handler("0", message, bot)

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call: types.CallbackQuery):
    handler(call.data, call.message, bot)

bot.infinity_polling()
