from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def main_keyboard() -> ReplyKeyboardMarkup:
    buttons = [
        [KeyboardButton(text="Добавить вес"), KeyboardButton(text="Добавить прием пищи")],
        [KeyboardButton(text="Сегодняшнее КБЖУ"), KeyboardButton(text="Статистика")],
    ]
    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
