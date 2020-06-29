from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.utils.markdown import hbold

from data.config import ADMINS_ID
from filters import IsPrivate
from loader import dp

from keyboards.inline.guardian_keyboard import generate_confirm_markup


@dp.message_handler(IsPrivate(), Command(commands="get_markup"), user_id=ADMINS_ID)
async def get_markup(message: types.Message):

    # Функция для тестов, которая не должна попасть в прод

    generated_tuple = generate_confirm_markup(message.from_user.id)

    markup = generated_tuple[0]
    subject = generated_tuple[1]

    await message.answer(f"Нажми на {hbold(subject)}",
                         reply_markup=markup,
    )
