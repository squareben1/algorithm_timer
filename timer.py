from timeit import default_timer as timer
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
        return [avg_time, func.__name__, len(args[0])]

    def print_results(self, time, name, array_length):
        average = '%.12f' % time
        print('Average time to run', name,
              'with an array', array_length, 'items long:', average)

    def graph_arr_generator(self, num_arrs, limit):
        output_arr = []
        step = limit // num_arrs
        for i in range(1, num_arrs+1):
            output_arr.append(list(range(1, (i * step)+1)))
        return output_arr


