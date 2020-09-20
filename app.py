import random
from grapher import create_graph
from timer import AlgoTimer
from arr_generators import *
import algorithms


class AlgoApp:
    def __init__(self, arr_num, arr_max):
        self.timer = AlgoTimer()
        self.test_arr = arr_generator(int(arr_num), int(arr_max))
        self.time_results = []
        self.arr_length = []

    def random_number_average(self, func, find_int=False):
        for arr in self.test_arr:
            time_res = []
            self.arr_length.append(len(arr))
            if find_int:
                for i in range(100):
                    output = self.timer.get_average(
                        func, arr, random.randint(0, len(arr)))
                    time_res.append(output[0])
                    # TODO EXTRACT these to own funcs
            else:
                for i in range(100):
                    output = self.timer.get_average(
                        func, arr)
                    time_res.append(output[0])
            average = sum(time_res) / len(time_res)
            self.time_results.append(average)
        return self.time_results, self.arr_length

    def run_search(self, method_to_call):
        time_results, arr_length = self.random_number_average(
            method_to_call, True)
        create_graph(time_results, arr_length, method_to_call.__name__)

    def run_sort(self, method_to_call):
        time_results, arr_length = self.random_number_average(
            method_to_call)
        create_graph(time_results, arr_length, method_to_call.__name__)

    def run_dups(self, method_to_call):
        self.test_arr = insert_dup(self.test_arr)

        time_results, arr_length = self.random_number_average(
            method_to_call)
        create_graph(time_results, arr_length, method_to_call.__name__)
        print(self.test_arr)

    def run(self, algorithm):
        method_to_call = getattr(algorithms, algorithm)
        if 'search' in algorithm:
            self.run_search(method_to_call)
        elif 'dups' in algorithm:
            self.run_dups(method_to_call)
        # else:
        #     self.run_sort(method_to_call)


if __name__ == "__main__":
    import sys
    import algorithms
    app = AlgoApp(sys.argv[1], sys.argv[2])
    app.run(sys.argv[3])

# TODO Tidy this up big time
# TODO fix find_dups so it isn't quadratic
# TODO write algorithms for shuffling, sorting and reversing
