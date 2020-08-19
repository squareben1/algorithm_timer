from timeit import default_timer as timer
from algorithms import *
import random

arr = list(range(10000000))

rand_num = random.randint(1, len(arr))


def basic_timer(func, *args):
    start = timer()
    func(*args)
    end = timer()
    value = end - start
    return value


def get_average(func, *args):
    total_time = 0
    for i in range(10):
        total_time += basic_timer(func, *args)
    avg_time = total_time / 10
    print('Average time to run', func.__name__,
          'with an array', len(args[0]), 'items long:')
    print('%.12f' % avg_time)


get_average(binary_search, arr, rand_num)
# get_average(random.shuffle(arr))
