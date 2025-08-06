from aiogram import Router
from aiogram.types import Message
from aiogram.filters.command import CommandStart
from keyboard import main_keyboard
router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(
        "Главное меню.",
        reply_markup=main_keyboard()
    )
