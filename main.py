
import asyncio
from app.bot import dp, bot

async def main():
    try:
        from aiogram import executor
        await dp.start_polling(bot, skip_updates=True)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(main())
