import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
from config import BOT_TOKEN, PROXY_URL
from apps.handlers import router

logging.basicConfig(level=logging.INFO)

if PROXY_URL:
    session = AiohttpSession(proxy=PROXY_URL)
    print("Бот запускается через прокси!")
else:
    session = AiohttpSession()
    print("Бот запускается без прокси (напрямую).")

bot = Bot(token=BOT_TOKEN, session=session)
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
