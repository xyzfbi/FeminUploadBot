from aiogram import Router
from aiogram.filters import Command
from aiogram.types import (
    Message,
)

import keyboards.keyboard as kb

router = Router()


@router.message(Command("help"))
async def start_command(message: Message):
    help_text = "заглушка"
    await message.reply(help_text, reply_markup=kb.main_keyboard())
