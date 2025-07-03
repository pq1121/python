import threading
import time
from random import randint as rd

def thread(num):
    print(f"Start thread {num}")
    rand_sleep = rd(1,6)
    time.sleep(rand_sleep)
    print(f"Stop thread {num}, time works {rand_sleep} seconds")

threads = []
rand_thread = rd(6,9)
for i in range(1, rand_thread):
    t = threading.Thread(target=thread, args=(i,))
    threads.append(t)

for t in threads:
    t.start()