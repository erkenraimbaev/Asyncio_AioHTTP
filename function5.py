import aiohttp
import asyncio
import time


# Асинхронная функция для загрузки содержимого URL
async def fetch_url(session, url):
    async with session.get(url) as response:
        return await response.text()


# Асинхронная функция для загрузки нескольких URL и измерения времени
async def fetch_multiple_urls(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_url(session, url) for url in urls]
        start_time = time.time()
        results = await asyncio.gather(*tasks)
        duration = time.time() - start_time
    print(f"Общее время загрузки: {duration:.2f} секунд")
    return results


# Основная функция для запуска
async def main():
    urls = [
        "https://example.com",
        "https://example.org",
        "https://example.net"
    ]
    results = await fetch_multiple_urls(urls)
    for i, result in enumerate(results):
        print(f"Содержимое {urls[i]}: {result[:100]}...")  # Выводим первые 100 символов содержимого


# Запуск основной функции
asyncio.run(main())
