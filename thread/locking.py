import threading
import time

# GOAL: myTestDB.value is to be incremeted to 2 using 2 threads

class myThread (threading.Thread):
   def __init__(self, name):
      threading.Thread.__init__(self)
      self.name = name
   def run(self):
      print(f"Starting {self.name}")
      # Lock to synchronize threads
      # threadLock.acquire()
      db.update()
      # Lock freed to release next thread
      # threadLock.release()

class myTestDB():
    def __init__(self):
        self.value = 0

    def update(self): 
        local_copy = self.value
        local_copy += 1
        time.sleep(0.1)
        self.value = local_copy # IMPORTANT: let me update the db

db = myTestDB()
threadLock = threading.Lock()
threads = list()
for index in range(2):
    x = myThread(f"Thread-{index}")
    threads.append(x)
    x.start()

for index, thread in enumerate(threads):
    thread.join() # wait for the threads 

print(f"myTestDB.value: {db.value}")
print("Exiting Main Thread")

# Without locking the threads:
# each thread will have their local copy of the value of the same db class, shared db object will create problem
