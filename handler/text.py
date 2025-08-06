from aiogram import Router, F
from aiogram.types import Message
from database import add_weight
router = Router()

@router.message(F.text == "Добавить вес")
async def add_weight_nadler(message: Message):
    await message.answer("Введите вес в килограммах")

@router.message(F.text)
async def process_weight(message: Message):
    try:
        text = message.text.strip().replace(",", ".")  # type: ignore
        
        if not text.replace(".", "").isdigit():
            await message.answer("Пожалуйста, введите число")
            return
            
        weight = float(text)
        
        if weight <= 0:
            await message.answer("Вес не может быть отрицательным или нулевым!")
            return
        elif weight > 200:
            await message.answer("Вес не может быть больше 200 кг!")
            return
        elif weight < 30:
            await message.answer("Вес не может быть меньше 30 кг!")
            return
            
        try:
            add_weight(weight)
            await message.answer(f"Вес {weight} кг успешно сохранён!")
        except Exception:
            await message.answer("Не удалось сохранить вес в базу данных. Пожалуйста, попробуйте позже.")
        
    except ValueError:
        await message.answer("Некорректный формат числа. Введите вес цифрами")
    except Exception as error:
        await message.answer(f"Произошла непредвиденная ошибка: {error}")
        print(f"Необработанная ошибка: {error}")