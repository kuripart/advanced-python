import asyncio

async def fetch():
    print('start')
    await asyncio.sleep(2)
    print('done')
    return {'test': 1}

async def num():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.5)

async def test():
    task_1 = asyncio.create_task(fetch())
    task_2 = asyncio.create_task(num())

    # start
    # 0

    val = await task_1
    print(val)
    await task_2

asyncio.run(test())