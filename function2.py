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
    urls = ['example.com', 'example1.com', 'example2.com']
    responses = [download_file(url) for url in urls]
    await asyncio.gather(*responses)
    count = 0
    for response in responses:
        count += 1
        print(f'{count}. {response}')


asyncio.run(main())
