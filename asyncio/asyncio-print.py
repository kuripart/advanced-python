import asyncio
import time

async def printasync(s):
    print(s)
    await asyncio.sleep(1)

# loop to execute my tasks
start = time.time()
loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(printasync("hi")),
    loop.create_task(printasync("bye!")),
]
loop.run_until_complete(asyncio.gather(*tasks)) # same as: loop.run_until_complete(asyncio.wait(*tasks))
loop.close()
end = time.time()
print(f'Time: {end-start:.2f} sec')
