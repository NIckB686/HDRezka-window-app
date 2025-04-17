import asyncio
from typing import Any, Callable, Coroutine

import aiohttp
from aiohttp import ClientResponse
from bs4 import BeautifulSoup, NavigableString

DEFAULT_URL = 'https://rezka.ag/'


async def get_content(url=DEFAULT_URL):
    async with aiohttp.ClientSession() as session:
        params = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36 Edg/135.0.0.0'
        }
        async with session.get(url, params=params) as resp:
            return await resp.text()


async def get_html(url=DEFAULT_URL):
    resp = await get_content(url)
    html = BeautifulSoup(resp, 'lxml')
    print(html.prettify())


class Page:
    def __init__(self, tag):
        ...

    async def _recursive_finder(self, node, results=None) -> list:
        if results is None:
            results = []
        if node.name == 'a':
            results.append([node.text.strip(), node.get('href', '') if node.get('href', '').startswith('h') else (
                    'https://rezka.ag' + node.get('href', ''))])
        elif isinstance(node, NavigableString):
            if node.strip() != '' and node.strip() != ':' and node.strip() != ',':
                results.append(node.strip())
        elif node.contents:
            for child in node.children:
                await self._recursive_finder(child, results)
        else:
            results.append(node.text.strip())
        return results

if __name__ == '__main__':
    asyncio.run(get_html())
