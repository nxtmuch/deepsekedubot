import asyncio
from aiogram import Bot, Dispatcher
from config import TG_TOKEN

from handlers import router


from telegram.ext import ApplicationBuilder, MessageHandler, filters

CHANNEL_ID = "-1002859508302"


async def main():
    bot = Bot(token=TG_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)



if __name__ == '__main__':
    try:
        app = ApplicationBuilder().token(TG_TOKEN).build()
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
