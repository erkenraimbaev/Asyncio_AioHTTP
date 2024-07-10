import aiohttp
import asyncio


async def fetch_data(session, url):
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.json()  # предполагаем, что сервер отдаёт JSON с числами
    except aiohttp.ClientError as e:
        print(f'Ошибка загрузки данных через {url}: {e}')
        return None


async def process_data():
    async with aiohttp.ClientSession() as session:
        urls = [
            '<http://example.com/data1>',
            '<http://example.com/data2>'
            '<http://example.com/data3>'
        ]
        tasks = [fetch_data(session, url) for url in urls]

        responses = asyncio.gather(*tasks)

        numbers = []

        for response in responses:
            if response is not None and 'number:':
                numbers.append(response['number'])

        if numbers:
            total_sum = sum(numbers)
            avg_number = total_sum / len(numbers)
            print(f'Total = {total_sum}')
            print(f'AVG = {avg_number}')
        else:
            print(f'We can not get numbers')


# Запуск асинхронной функции
if __name__ == '__function1__':
    asyncio.run(process_data())
