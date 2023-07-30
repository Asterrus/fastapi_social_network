import aiohttp

from config import HUNTER_URL, HUNTER_IO_API_KEY


async def get_email_status(email):
    url = f"{HUNTER_URL}?email={email}&api_key={HUNTER_IO_API_KEY}"
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response_json = await response.json()
            return response_json['data']['status']
