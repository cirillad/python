from aiogram import Bot, Dispatcher
from dotenv import find_dotenv, load_dotenv
import os
import asyncio
from handlers.user_private import user_private_router

load_dotenv(find_dotenv())
bot = Bot(token=os.getenv('TOKEN'))
dp = Dispatcher()
dp.include_router(user_private_router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())
