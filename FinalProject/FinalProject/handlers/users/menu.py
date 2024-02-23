import os
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import Command
from aiogram import types
from aiogram.types import InputFile
from loader import dp, bot
from parser.olx_methods import start_parse
from utils.check_value import check_value_of_message


@dp.message_handler(Command('start_parsing'), state=(None, '*'))
async def start_bot_function(message: types.Message, state: FSMContext):
    text = "<b>Скільки об'яв ви хочете отримати?</b>"

    await message.answer(text)

    await state.set_state('entering_number')


@dp.message_handler(state='entering_number')
async def anser_json_file(message: types.Message, state: FSMContext):

    checking_value = check_value_of_message(message.text)

    if not checking_value:
        text = "<b>Введіть цифру корректно або ж зменшіть її до 50</b>"

        await message.answer(text)

        return

    text2 = '<b>Розпочинаємо парсинг</b>'
    await message.answer(text2)

    result = start_parse(amount_of_parse=int(message.text), id_telegram=message.from_user.id)

    path_with_file = f'{message.from_user.id}_data.json'

    file_for_input = InputFile(path_with_file)


    await message.answer_document(document=file_for_input)

    os.remove(path_with_file)

    await state.finish()
