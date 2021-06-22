import aiohttp
import asyncio
import async_timeout
import time
import os
import requests

# Asynchronous HTTP requests

# Tutorial: https://www.twilio.com/blog/asynchronous-http-requests-in-python-with-aiohttp

# Asynchronous code is code that can hang while waiting for a result, in order to let other code run in the meantime. 
# It doesn't "block" other code from running so we can call it "non-blocking" code.

async def main():

    # https://docs.aiohttp.org/en/latest/http_request_lifecycle.html#how-to-use-the-clientsession
    async with aiohttp.ClientSession() as session:

        pokemon_url = 'https://pokeapi.co/api/v2/pokemon/151'
        async with session.get(pokemon_url) as resp:
            pokemon = await resp.json()
            print(pokemon['name'])

# RuntimeError: Event loop is closed: https://stackoverflow.com/a/66772242
# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
# asyncio.run(main())


# ASYNC

# start_time = time.time()

async def largerequest():

    async with aiohttp.ClientSession() as session:

        for number in range(1, 25):
            pokemon_url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            async with session.get(pokemon_url) as resp:
                pokemon = await resp.json() # while you wait go and grab another request
                print(pokemon['name'])

# asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
# asyncio.run(largerequest())
# print("--- %s seconds ---" % (time.time() - start_time))


# SYNC
# For each consecutive request, we have to wait for the previous step to finish before even beginning the process

start_time = time.time()

for number in range(1, 25):
    url = f'https://pokeapi.co/api/v2/pokemon/{number}'
    resp = requests.get(url)
    pokemon = resp.json()
    print(pokemon['name'])

print("--- %s seconds ---" % (time.time() - start_time))