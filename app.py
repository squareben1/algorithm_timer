from timer import AlgoTimer
from algorithms import *
import random

class AlgoApp:

    def __init__(self, arr_num, arr_max):
        self.timer = AlgoTimer()
        self.test_arr = self.timer.graph_arr_generator(arr_num, arr_max)
        self.time_results = []
        self.arr_length = []

    def run_tests(self, func):
        for arr in self.test_arr:
            output = self.timer.get_average(func, arr, random.randint(0, len(arr)))
            self.time_results.append(output[0])
            self.arr_length.append(output[2])
        return self.time_results, self.arr_length

app = AlgoApp(20, 100_000)
print(app.run_tests(binary_search))
