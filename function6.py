import asyncio


async def show_argument(arg: str):
    await asyncio.sleep(2)
    print(arg)


async def print_argument(arg: str):
    await asyncio.sleep(2)
    print(arg)


async def show_arguments():
    arguments = []
    arguments.append(show_argument('Hello'))
    arguments.append(print_argument('World'))
    await asyncio.gather(*arguments)
    for i in arguments:
        print(i)


asyncio.run(show_arguments())
