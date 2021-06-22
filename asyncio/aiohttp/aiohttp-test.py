import aiohttp
import asyncio
import async_timeout
import time
import os
import requests

MAX = 10

# Asynchronous HTTP requests

# Tutorial: https://www.twilio.com/blog/asynchronous-http-requests-in-python-with-aiohttp

# Asynchronous code is code that can hang while waiting for a result, in order to let other code run in the meantime. 
# It doesn't "block" other code from running so we can call it "non-blocking" code.


# FOR mock api testing: https://jsonplaceholder.typicode.com/

async def main():

    # https://docs.aiohttp.org/en/latest/http_request_lifecycle.html#how-to-use-the-clientsession
    async with aiohttp.ClientSession() as session:

        url = 'https://jsonplaceholder.typicode.com/todos/1'
        async with session.get(url) as resp:
            data = await resp.json()
            print(data['name'])

## Comment out to test
# RuntimeError: Event loop is closed: https://stackoverflow.com/a/66772242
# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
# asyncio.run(main())

# ASYNC
print("async request...")
start_time = time.time()

async def largerequest():

    async with aiohttp.ClientSession() as session:

        for number in range(1, MAX):
            url = f'https://jsonplaceholder.typicode.com/todos/{number}'
            async with session.get(url) as resp:
                data = await resp.json() # while you wait go and grab another request; await on each HTTP request
                print(data['title'])

# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy()) ## THIS IS FOR WINDOWS
asyncio.run(largerequest())
print("--- %s seconds ---" % (time.time() - start_time))


# FOR MAC: 
# aiohttp.client_exceptions.ClientConnectorCertificateError: 
# Cannot connect to host jsonplaceholder.typicode.com:443 ssl:True [SSLCertVerificationError: (1, '[SSL: CERTIFICATE_VERIFY_FAILED] 
# certificate verify failed: unable to get local issuer certificate (_ssl.c:1076)')]
# Solution:
# https://stackoverflow.com/a/58525755

# SYNC
# For each consecutive request, we have to wait for the previous step to finish before even beginning the process
print("sync request...")
start_time = time.time()

for number in range(1, MAX):
    url = f'https://jsonplaceholder.typicode.com/todos/{number}'
    resp = requests.get(url)
    data = resp.json()
    print(data['title'])

print("--- %s seconds ---" % (time.time() - start_time))
