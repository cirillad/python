from aiogram import types, Router
from aiogram.filters import CommandStart, Command

user_private_router = Router()


@user_private_router.message(Command('menu'))
async def menu_cmd(message: types.Message):
    await message.answer('Menu :\n1. /start\n 2. /menu\n 3. /help\n 4. /echo')


@user_private_router.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Hello, I`m your bot')


@user_private_router.message(Command('help'))
async def help(message: types.Message):
    await message.answer('How can I help you?')


@user_private_router.message()
async def echo(message: types.Message):
    await message.answer(message.text)



