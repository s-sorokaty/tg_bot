import asyncio

from telebot import types
from telebot.async_telebot import AsyncTeleBot

from config import settings
from exceptions import BotAccessError


def check_access(func):
    async def wrapper(*arg, **kwarg):
        message: types.Message = arg[0]
        if message.from_user.id not in settings.ACCESS_USER_IDS:
            res = await func(*arg, **kwarg)
            return res
        else:
            await BotAccessError('Access Error').access_denied_message(message)
    return wrapper