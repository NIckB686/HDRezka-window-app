import asyncio

import aiohttp

DEFAULT_URL = 'https://rezka.ag/'

class Fetcher:
    """Класс для асинхронной загрузки данных с сайта"""

    def __init__(self):
        self.session = None

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.session.close()

    async def get_html(self, url: str) -> str:
        async with self.session.get(url) as responce:
            return await responce.text()

    async def get_image(self, url: str) -> bytes:
        async with self.session.get(url) as responce:
            return await responce.read()

    async def get_images_batch(self, urls: list[str]) -> list[bytes]:
        tasks = [self.get_image(url) for url in urls]
        return await asyncio.gather(*tasks)
