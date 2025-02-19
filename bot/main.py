from telebot import types, TeleBot
from db.init import init as db_init

from config import Settings

from handler import handler
from question import Test

settings = Settings()
db_init()
bot = TeleBot(settings.BOT_TOKEN)

@bot.message_handler(commands = ['start'])
def url(message: types.Message):
    Test.draw_hello_message(message, bot)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call: types.CallbackQuery):
    handler(call.data, call.message, bot)


bot.infinity_polling()
