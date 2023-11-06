
import requests
from aiogram import Bot
from aiogram import types as tg_types
from aiogram import Dispatcher
from aiogram import filters,executor

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, \
    KeyboardButton
import sqlite3
from config import tg_token

tgbot = Bot(tg_token)
dp=Dispatcher(tgbot)
@dp.message_handler(commands=['start'])
async def message_handler(message:tg_types.Message):
    await message.answer('привет')

if __name__ == '__main__':
    executor.start_polling(dp)