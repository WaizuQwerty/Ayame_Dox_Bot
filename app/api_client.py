
import aiohttp
from app.config import settings

async def get_phone_info(phone):
    headers = {"X-Auth": settings.PROBIVAPI_KEY}
    url = f"https://callerapi.com/api/phone/info/{phone}"

    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers) as response:
            response.raise_for_status()
            return await response.json()
