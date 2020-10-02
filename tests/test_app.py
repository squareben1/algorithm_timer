import pytest

from app import AlgoApp

subject = AlgoApp(10, 5)

arr_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_slice_outlier_results():
    arr_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected = [2, 3, 4, 5, 6, 7, 8, 9]
    assert subject.slice_outlier_results(arr_input) == expected


def test_get_average_selected_time_data():
    sliced_arr = [2, 3, 4, 5, 6, 7, 8, 9]
    expected = sum(sliced_arr) / len(sliced_arr)
    assert subject.get_average_selected_time_data(arr_input) == expected
