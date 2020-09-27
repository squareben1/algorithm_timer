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


    def run(self, algorithm):
        self.set_test_arr(algorithm)
        self.loop_over_array(algorithm)

        create_graph(self.time_results, self.arr_length,
                     algorithm)


    def set_test_arr(self, algorithm):
        if 'dups' in algorithm:
            self.test_arr = insert_dup(self.test_arr)


    def loop_over_array(self, algorithm):
        algorithm_to_time = getattr(algorithms, algorithm)
        selected_function_type = self.select_function_type(algorithm)
        
        for arr in self.test_arr:
            self.collate_and_set_timing_data(arr, algorithm_to_time, selected_function_type)


    def select_function_type(self, algorithm):
        if 'search' in algorithm:
            return self.search_random_number
        else:
            return self.run_non_search_algorithm


    def collate_and_set_timing_data(self, arr, algorithm_to_time, selected_function_type):
        self.arr_length.append(len(arr))
        result = self.run_algorithm(algorithm_to_time, arr, selected_function_type)
        self.time_results.append(
            self.get_average_selected_time_data(result))


    def search_random_number(self, func, arr):
        return self.timer.get_average(
                func, arr, random.randint(0, len(arr)))


    def run_non_search_algorithm(self, func, arr):
        return self.timer.get_average(
                func, arr)


    def run_algorithm(self, func, arr, selected_function_type):
        hold_arr = []
        for i in range(self.run_times):
            output = selected_function_type(func, arr)
            hold_arr.append(output[0])
        return hold_arr


    def get_average_selected_time_data(self, result):
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
    app.run(sys.argv[3])

# TODO write algorithms for shuffling, sorting and reversing
# TODO remove number of arrays as argument
