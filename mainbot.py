import asyncio

from aiogram import Bot, Dispatcher
from config import UNUSE_TOKEN, TEST_TOKEN, MAIN_TOKEN
from apps.handlers import router

bot = Bot(token=TEST_TOKEN)

dp = Dispatcher()
async def main():
    dp.include_router(router)
    await dp.start_polling(bot)
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')


