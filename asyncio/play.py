import asyncio
from time import sleep


async def run_test_1(): #coroutine(): #coroutine
  print('test 1')
  task = asyncio.create_task(run_test_2())
  print('done')

async def run_test_2(): #coroutine
  print('test 2')
  await asyncio.sleep(1)



asyncio.run(run_test_1()) #coroutine())
