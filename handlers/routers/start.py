from aiogram import Router
from aiogram.filters import Command
from aiogram.types import (
    Message,
)

import keyboards.keyboard as kb

router = Router()


@router.message(Command("start"))
async def start_command(message: Message):
    user_id = message.chat.id
    keyboard = kb.main_keyboard()
    user_name = message.from_user.username
    welcome_text = (
        f"Здарова, @{user_name}!"
        f"\n\nЯ робот для загрузки треков на площадку Femin"
        f"\n\nAvailable commands: /start, /help, /yandex"
        f"\nПанкуха, выбирай одну их коммкнд снизу и погнали!"
    )

    await message.reply(welcome_text, reply_markup=keyboard)
