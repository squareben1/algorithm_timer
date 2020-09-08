import random
from grapher import create_graph
from timer import AlgoTimer
from algorithms import *


class AlgoApp:
    def __init__(self, arr_num, arr_max, timer):
        self.timer = timer
        self.test_arr = self.graph_arr_generator(arr_num, arr_max)
        self.time_results = []
        self.arr_length = []

    def graph_arr_generator(self, num_arrs, limit):
        output_arr = [[]]
        step = limit // num_arrs
        for i in range(1, num_arrs+1):
            output_arr.append(list(range(1, (i * step)+1)))
        return output_arr

    def run_tests(self, func):
        for arr in self.test_arr:
            time_res = []
            self.arr_length.append(len(arr))
            for i in range(1000):
                output = self.timer.get_average(func, arr, random.randint(0, len(arr)))
                time_res.append(output[0])
            average = sum(time_res) / len(time_res)
            self.time_results.append(average)
        return self.time_results, self.arr_length

timer = AlgoTimer()
app = AlgoApp(50, 10_000_000, timer)
time_results, arr_length = app.run_tests(binary_search)

create_graph(time_results, arr_length)

