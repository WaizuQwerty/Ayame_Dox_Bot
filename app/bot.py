
from aiogram import Bot, Dispatcher
from app.config import settings

bot = Bot(token=settings.TELEGRAM_API_TOKEN)
dp = Dispatcher()
