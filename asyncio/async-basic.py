import asyncio
from time import sleep

async def run_test_1():
    # print('asynchronous')
    # await run_test_2('test')
    # print('done')
    
    ## RESULT
    # asynchronous
    # test
    # done

    print('asynchronous')
    task = asyncio.create_task(run_test_2('test'))
    # await task ## will give the first result
    # await asyncio.sleep(2) ## will give the first result
    print('done')

    ## RESULT
    # asynchronous
    # done
    # test

async def run_test_2(test):
    print(test)
    await asyncio.sleep(1) # cannot use this outside an asynchronous function
    
    

asyncio.run(run_test_1())
# asyncio.run(run_test_2('test'))