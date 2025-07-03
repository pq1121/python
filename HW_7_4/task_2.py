from threading import Thread
import time
from random import randint as rd


class MyThread(Thread):

    def __init__(self, num, delay):
        super().__init__()
        self.__num = num
        self.__delay = delay

    def run(self):
        print(f"Start {self.__num} thread")
        time.sleep(self.__delay)
        print(f"Stop {self.__num} thread , time works {self.__delay} seconds")


rand_thread = rd(6,9)

for i in range(1, rand_thread):
    rand_delay = rd(1, 6)
    t = MyThread(i, rand_delay)
    t.start()