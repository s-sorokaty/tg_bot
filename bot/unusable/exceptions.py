from telebot import types
from config import settings
from telebot.async_telebot import AsyncTeleBot


class BotError(Exception):
    def __init__(self, message: types.Message):
        self.message: types.Message = message
        self.bot: AsyncTeleBot = AsyncTeleBot(settings.BOT_TOKEN)
    def __str__(self):
        return self.message

class BotAccessError(BotError):
    async def access_denied_message(self, message:types.Message):
        await self.bot.reply_to(message, 'Access Denied')
        raise BotAccessError(f'Access Denied for user {message.from_user.id}')