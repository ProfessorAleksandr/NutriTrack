import asyncio
from colorama import Fore, init
from config import Config
from aiogram import Bot, Dispatcher, Router
from handler import commands_router,text_router,callbacks_router
from database import init_db
async def main() -> None:
    try:
        init_db()
        bot = Bot(Config.API_TOKEN)
        dp = Dispatcher()
        dp.include_router(commands_router)
        dp.include_router(text_router)
        dp.include_router(callbacks_router)
        init()
        print(Fore.GREEN + "Бот запущен")
        await dp.start_polling(bot)
    except Exception as error:
        print(Fore.RED + f"Бот сломался по ошибке: {error}")


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt as error:
        print(Fore.BLUE + f"Бот выключен")
    except Exception as error:
        print(Fore.RED + f"Бот выключен по ошибке: {error}")
