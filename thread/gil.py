
import time
from threading import Thread

MX = 30000000

# single
def countdown(count):
    while count:
        count = count - 1

start = time.time()
countdown(MX)
end = time.time()

print('Time taken for single threaded: ', end - start)


# multi
t1 = Thread(target=countdown, args=(MX//2,))
t2 = Thread(target=countdown, args=(MX//2,))

start = time.time()
t1.start()
t2.start()
t1.join()
t2.join()
end = time.time()

print('Time taken for multi threaded: ', end - start)