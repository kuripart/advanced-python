import time
import threading
import concurrent.futures

def test(name):
    print(f"starting {name}")
    time.sleep(2)
    print(f"done {name}")

# this .join() s the threads
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor: # max_workers -> worker threads
    executor.map(test, range(1)) # range() --> how many call to the test function

    # 1 worker; 4 calls --> more work for 1 thread, over processing
    # 3 wrokers; 1 call --> less work, many threads, waste of recources

