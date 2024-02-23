from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram import types
from loader import dp


@dp.message_handler(CommandStart(), state=(None, '*'))
async def start_bot_function(message: types.Message):
    text = '<b>Доброго дня 👋🏻</b>'
    await message.answer(text)