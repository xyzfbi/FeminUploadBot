from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def main_keyboard() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="/yandex")],
            [KeyboardButton(text="/start")],
            [KeyboardButton(text="/help")],
        ],
        resize_keyboard=True,
        one_time_keyboard=False,
    )
    return keyboard
