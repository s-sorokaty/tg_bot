from telebot import types, TeleBot
from telebot.custom_filters import TextFilter, TextMatchFilter, IsReplyFilter

from config import Settings
from handler import handler
from db.init import init as db_init

settings = Settings()
db_init()
bot = TeleBot(settings.BOT_TOKEN)

@bot.message_handler(commands = ['start'])
def url(message: types.Message):
    handler("0", message, bot)

@bot.message_handler(commands = ['politics'])
def url(message: types.Message):
        bot.send_document(
            chat_id=message.chat.id, 
            document=open('Политика конфеденциальности.pdf', 'rb'),
        )

@bot.callback_query_handler(func=None)
def callback_inline(call: types.CallbackQuery):
    handler(call.data, call.message, bot)

bot.infinity_polling()
