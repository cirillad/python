from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("start_parsing", "Розпачати парсинг"),
        types.BotCommand("start", "Розпочати роботу з ботом"),
    ])