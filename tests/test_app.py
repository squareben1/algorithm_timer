import pytest

from app import AlgoApp

subject = AlgoApp(10, 5)

arr_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_slice_outlier_results():
    arr_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected = [2, 3, 4, 5, 6, 7, 8, 9]
    assert subject.slice_outlier_results(arr_input) == expected


def test_get_average_selected_time_data():
    assert subject.get_average_selected_time_data(arr_input) == 5.5


def dummy_algorithm(arr):
    return arr[0]


def test_run_algorithm_on_non_search_algo():
    output = subject.run_algorithm(
        dummy_algorithm, arr_input, subject.run_non_search_algorithm)
    assert len(output) == subject.run_times
