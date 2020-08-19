from timeit import default_timer as timer
from algorithms import *
import random

arr = list(range(10000000))

rand_num = random.randint(1, len(arr))


class AlgoTimer:
    def __init__(self):
        self.avgs_arr = []

    def basic_timer(self, func, *args):
        start = timer()
        func(*args)
        end = timer()
        value = end - start
        return value

    def get_average(self, func, *args):
        total_time = 0
        for i in range(10):
            total_time += self.basic_timer(func, *args)
        avg_time = total_time / 10
        # print('Average time to run', func.__name__,
        #       'with an array', len(args[0]), 'items long:')
        # average = '%.12f' % avg_time
        return avg_time

    def graph_arr_generator(self, interval, limit):
        if limit == 1:
            return [[1]]
        else:
            return [[1], [1, 2]]
# steps = limit // interval
        # for i in range(1, steps + 1):
        #     arr = list(range(i * interval))
        #     return arr


# algo_timer = AlgoTimer()

# algo_timer.get_average(binary_search, arr, rand_num)
# get_average(random.shuffle(arr))
