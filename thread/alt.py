# Alternate way of working with threads from: 
# https://www.tutorialspoint.com/python/python_multithreading.htm

import _thread # thread in older py versions < 3.
import time

# Define a function for the thread
def print_time( threadName, delay):
   count = 0
   while count < 2:
      time.sleep(delay)
      count += 1
      print(f"{threadName} {time.ctime(time.time())}")

_thread.start_new_thread( print_time, ("Thread1", 1, ) ) # ("Thread-1", 2, ) args that go into print_time
_thread.start_new_thread( print_time, ("Thread2", 2, ) )


# downside of using this low level threading, have main() wait indefinetly...
while True:
  time.sleep(10)
  break
