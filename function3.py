import asyncio


async def download_file(url: str):
    try:
        if 'error' in url:
            raise Exception('Error')
        print(f'Download starts from {url}')
        await asyncio.sleep(3)
        print('File is downloaded')
    except Exception as e:
        print(f'I can not download from: {e}')


async def main():
    urls = ['error1.com', 'error.com', 'example2.com']
    tasks = []
    for url in urls:
        task = download_file(url)
        tasks.append(task)
    # responses = [download_file(url) for url in urls if 'error' not in url]
    await asyncio.gather(*tasks)
    count = 0
    for response in tasks:
        count += 1
        print(f'{count}. {response}')


asyncio.run(main())
