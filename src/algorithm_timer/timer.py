from timeit import default_timer as timer
import random


class AlgoTimer:
    def basic_timer(self, func, *args):
        start = timer()
        func(*args)
        end = timer()
        value = end - start
        return value

    def get_average(self, func, *args):
        total_time = 0
        run_times = 50
        for i in range(run_times):
            total_time += self.basic_timer(func, *args)
        avg_time = total_time / run_times

        self.print_results(avg_time)
        return [avg_time, len(args[0])]

    def print_results(self, time):
        average = '%.12f' % time
        print('Average time: ', average)
