import concurrent.futures
import time
import threading

# GOAL: myTestDB.value is to be incremented to 2 using 2 threads

class myTestDB():
    def __init__(self):
        self.value = 0
        self._lock = threading.Lock()

    def update(self, name):
        with self._lock:
            local_copy = self.value
            local_copy += 1
            time.sleep(0.1)
            self.value = local_copy # IMPORTANT: let me update the db

db = myTestDB()
print(f"Start myTestDB.value: {db.value}")
with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
    executor.map(db.update, range(2))

print(f"Final myTestDB.value: {db.value}")
print("Exiting Main Thread")
