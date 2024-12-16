
import logging
from aiogram.types import Message
from app.bot import dp
from app.api_client import get_phone_info
from app.utils import format_response
from app.cache import cache

logger = logging.getLogger(__name__)

@dp.message(commands=['start', 'help'])
async def send_welcome(message: Message):
    await message.reply("Добро пожаловать! Отправьте номер телефона для анализа.")

@dp.message()
async def process_phone_number(message: Message):
    phone = message.text.strip()
    if not phone.startswith('+'):
        await message.reply("Пожалуйста, отправьте номер в формате +1234567890.")
        return

    # Проверка в кэше
    if phone in cache:
        response = cache[phone]
    else:
        response = await get_phone_info(phone)
        cache[phone] = response

    formatted_response = format_response(response)
    await message.reply(formatted_response)
