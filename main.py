import asyncio
import logging
from aiogram import Bot, Dispatcher
from app.database.models import db, User, Group, Work
from config import TOKEN
import app


bot = Bot(token = TOKEN)
dp = Dispatcher()

#
async def main():
    dp.include_router(app.router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    db.connect()
    db.create_tables([User, Group, Work])
    db.close()

    logging.basicConfig(level = logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')