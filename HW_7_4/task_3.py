import threading
import time
from random import randint as rd


def thread(num):
    global count_threads
    time.sleep(rd(1,5))
    count_threads = count_threads + 1
    print(f"Count Threads {count_threads}")

count_threads = 0
threads = []
rand_thread = rd(56,69)
for i in range(1, rand_thread):
    t = threading.Thread(target=thread, args=(i,))
    threads.append(t)

for t in threads:
    t.start()