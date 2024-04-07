import asyncio
import logging
from aiogram import Bot, Dispatcher
from app.handlers import router
from app.database.models import db, User
from config import TOKEN


bot = Bot(token = TOKEN)
dp = Dispatcher()


async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    db.connect()
    db.create_tables([User])
    db.close()

    logging.basicConfig(level = logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')