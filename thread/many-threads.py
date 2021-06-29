import threading
import time

def test(name):
    print(f"starting {name}")
    time.sleep(2)
    print(f"done {name}")

threads = []
for index in range(3):
    print(f"start thread {index}")
    x = threading.Thread(target=test, args=(index,))
    threads.append(x)
    x.start()

for index, thread in enumerate(threads):
    thread.join() # wait for the threads 
    print(f"main done {index}")

# The order in which threads are run are determined by the OS
