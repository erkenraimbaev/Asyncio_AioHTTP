import asyncio
from urllib.parse import urlparse

import aiohttp


async def download_and_save_to_file(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            data = await response.text()
            hostname = urlparse(url).hostname
            if hostname:
                print(hostname)
                filename = str(hostname) + '.txt'
                with open(filename, mode='w', encoding='utf-8') as file:
                    file.write(data[:30])
            else:
                print('Hostname is NONE')
    return await response.text()


async def main():
    urls = [
        'https://yandex.ru',
        'https://google.com'
    ]
    responses = [download_and_save_to_file(url) for url in urls]
    await asyncio.gather(*responses)


asyncio.run(main())
