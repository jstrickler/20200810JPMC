from threading import Thread, Lock
import time
import random

stdout_lock = Lock()

def hello(num):
    time.sleep(random.randint(1, 3))
    with stdout_lock:
        print("hello", num)

for i in range(10):
    t = Thread(target=hello, args=(i,))
    t.start()
print("All threads launched")