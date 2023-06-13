from multiprocessing import Process, Queue
import random

from datetime import datetime
from vj_zad1 import print_machine_info

t1 = datetime.now()
print_machine_info()
print("Vrijeme početka skeniranja je: ", t1)

def rand_num():
    num = random.random()
    print ("\n %f" % num)


if __name__ == "__main__":
    queue = Queue()
    processes = [Process(target=rand_num, args=()) for x in range(4)]
    for p in processes:
        p.start()
    for p in processes:
        p.join()
