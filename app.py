import random
from grapher import create_graph
from timer import AlgoTimer
from arr_generators import *
from algorithms import *


class AlgoApp:
    def __init__(self, arr_num, arr_max, timer):
        self.timer = timer()
        self.test_arr = arr_generator(arr_num, arr_max)
        self.time_results = []
        self.arr_length = []

    def random_number_average(self, func):
        for arr in self.test_arr:
            time_res = []
            self.arr_length.append(len(arr))
            for i in range(2000):
                output = self.timer.get_average(
                    func, arr, random.randint(0, len(arr)))
                time_res.append(output[0])
            average = sum(time_res) / len(time_res)
            self.time_results.append(average)
        return self.time_results, self.arr_length

    def run(self, algorithm):
        time_results, arr_length = self.random_number_average(algorithm)
        create_graph(time_results, arr_length, algorithm.__name__)


app = AlgoApp(20, 10_000, AlgoTimer)
app.run(binary_search)

# TODO: add final line to command line output giving overall average & func.__name__

# if __name__ == "__main__":
#     import sys
#     app = AlgoApp(sys.argv[0], sys.argv[1], AlgoTimer)
