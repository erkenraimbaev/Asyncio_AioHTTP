import aiohttp
import asyncio


async def download_file(url: str):
    try:
        print(f'Download starts from {url}')
        await asyncio.sleep(3)
        print('File is downloaded')
    except aiohttp.ClientError as e:
        print(f'Ошибка запроса клиента: {e}')


async def main():
    await download_file('https://download.com/image/')


asyncio.run(main())
