import multiprocessing as mp

from datetime import datetime
from vj_zad1 import print_machine_info

t1 = datetime.now()
print_machine_info()
print("Vrijeme početka skeniranja je: ", t1)

def my_func(x):
    print(x**x)  # x na potenciju x


def main():
    pool = mp.Pool(mp.cpu_count())
    result = pool.map(my_func, [4, 2, 3])


if __name__ == "__main__":
    main()
