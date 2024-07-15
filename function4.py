import aiohttp
import time
import asyncio


async def fetch_url(url: str):
    async with aiohttp.ClientSession as session:
        async with session.get(url) as response:
            return await response.text()


async def fetch_all(urls: list):
    start_time = time.time()
    results = []
    for url in urls:
        result = fetch_url(url)
        results.append(result)
    print(f"Длительность: {time.time() - start_time}")
    responses = asyncio.gather(*results)
    return responses




if __name__ == '__main__':
    asyncio.run(fetch_all(urls=urls))
