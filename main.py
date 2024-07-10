import aiohttp
import asyncio


async def get_data(url):
    async with aiohttp.ClientSession() as session:
        try:
            async with session.get(url) as response:
                return await response.text()
        except aiohttp.ClientError as client_error:
            print(f'Client error: {client_error}')
        except aiohttp.ServerConnectionError as server_error:
            print(f'Server error: {server_error}')
        finally:
            await session.close()


async def main():
    url1 = get_data('<http://example.com/data1>')
    url2 = get_data('<http://example.com/data2>')
    url3 = get_data('<http://example.com/data3>')

    task1 = asyncio.create_task(get_data(url1))
    task2 = asyncio.create_task(get_data(url2))
    task3 = asyncio.create_task(get_data(url3))

    data1 = await task1
    data2 = await task2
    data3 = await task3

    print(data1)
    print(data2)
    print(data3)


if __name__ == '__main__':
    asyncio.run(main())
