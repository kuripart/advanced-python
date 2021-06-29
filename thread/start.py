import threading
import time

def test(name):
    print(f"start {name}")
    time.sleep(2)
    print(f"done {name}")

# daemon v non-daemon

# x = threading.Thread(target=test, args=(1,)) # Non-daemon
# x.start()
# print("done main -- non daemon eg.")

# Non daemon threads in a program are waited upon. 
# Daemon threads are killed when the program is exiting.

y = threading.Thread(target=test, args=(999,), daemon=True) # Daemon
y.start()
# start v run --> run will explicitly run the thread, it does not spawn or create threads 
y.setName('Bond, James Bond') # my name is ...
print(f"{y.getName() }") # say my name!
print(f"{y.isAlive() }") # am i alive?
# y.join() # Join main thread with y thread --> to wait till its execution is over
print("done main -- daemon eg.")




