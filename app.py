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
        self.run_times = 5

    def select_run_type(self, algorithm):
        method_to_call = getattr(algorithms, algorithm)
        if 'search' in algorithm:
            self.get_average_with_random_num(method_to_call, True)
        elif 'dups' in algorithm:
            self.test_arr = insert_dup(self.test_arr)
            self.get_average_with_random_num(method_to_call)
        else:
            self.get_average_with_random_num(method_to_call)

        create_graph(self.time_results, self.arr_length, method_to_call.__name__)

    def get_average_with_random_num(self, func, find_int=False):  # rename
        for arr in self.test_arr:
            self.arr_length.append(len(arr))
            if find_int:
                result = self.search_for_random_num(func, arr)
            else:
                result = self.run_sort_algo(func, arr)

            self.time_results.append(self.get_average(result))
        return self.time_results, self.arr_length

    def search_for_random_num(self, func, arr):
        hold_arr = []
        for i in range(self.run_times):
            output = self.timer.get_average(
                func, arr, random.randint(0, len(arr)))
            hold_arr.append(output[0])
        return hold_arr

    def run_sort_algo(self, func, arr):
        hold_arr = []
        for i in range(self.run_times):
            output = self.timer.get_average(
                func, arr)
            hold_arr.append(output[0])
        return hold_arr

    def get_average(self, result):
        sliced_results = self.slice_outlier_results(result)
        average = sum(sliced_results) / len(sliced_results)
        return average

    def slice_outlier_results(self, results_array):
        results_array = sorted(results_array)
        for time in results_array:
            pc_to_cut = len(results_array) // 10
            end_slice = len(results_array) - pc_to_cut
        return results_array[pc_to_cut:end_slice]

if __name__ == "__main__":
    import sys
    import algorithms
    app = AlgoApp(sys.argv[1], sys.argv[2])
    app.select_run_type(sys.argv[3])

# TODO write algorithms for shuffling, sorting and reversing
# TODO remove number of arrays as argument 
