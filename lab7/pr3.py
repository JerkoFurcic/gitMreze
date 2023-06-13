import multiprocessing as mp

from datetime import datetime
from vj_zad1 import print_machine_info

t1 = datetime.now()
print_machine_info()
print("Vrijeme početka skeniranja je: ", t1)

def my_func(x):
    print(mp.current_process())
    return x**x


def main():
    pool = mp.Pool(mp.cpu_count())
    result = pool.map(my_func, [4, 2, 3, 5, 3, 2, 1, 2])
    result_set_2 = pool.map(my_func, [4, 6, 5, 4, 6, 3, 23, 4, 6])
    print(result)
    print(result_set_2)


if __name__ == "__main__":
    main()
