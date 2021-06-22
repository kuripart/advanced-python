import aiohttp
import asyncio
import time

MAX=10

start_time = time.time()

## tasks: responsible for the execution of coroutines within an event loop

async def get_data(session, url):
    async with session.get(url) as resp:
        data_ = await resp.json()
        return data_['title']


async def main():
    async with aiohttp.ClientSession() as session:

        tasks = []
        for number in range(1, MAX):
            url = f'https://jsonplaceholder.typicode.com/todos/{number}'
            # Future Object
            # class asyncio.Future(*, loop=None)
            # A Future represents an eventual result of an asynchronous operation. Not thread-safe.

            # Future is an awaitable object. Coroutines can await on Future objects until they either have a result or an exception set, or until they are cancelled.
            # tasks.append(asyncio.ensure_future(get_data(session, url)))
            tasks.append(asyncio.create_task(get_data(session, url)))

        # https://stackoverflow.com/a/44614131
        # asyncio.gather mainly focuses on gathering the results. It waits on a bunch of futures and returns their results in a given order
        data__ = await asyncio.gather(*tasks) 

        print(data__) ## LIST
        for data in data__:
            print(data)

asyncio.run(main())
print("--- %s seconds ---" % (time.time() - start_time))
