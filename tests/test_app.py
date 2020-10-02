import pytest
import mock
from unittest.mock import Mock, patch

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


def test_collate_and_set_timing_data():
    output = subject.collate_and_set_timing_data(
        arr_input, dummy_algorithm, subject.run_non_search_algorithm)
    assert subject.arr_length[0] == len(arr_input)
    assert type(subject.time_results[0]) is float


def test_select_algorithm_type_search():
    assert subject.select_algorithm_type(
        'binary_search') == subject.search_random_number


def test_select_algorithm_type_non_search():
    assert subject.select_algorithm_type(
        'find_dups') == subject.run_non_search_algorithm


def test_loop_over_array():
    with mock.patch('app.AlgoApp.collate_and_set_timing_data') as mock_collate:
        subject.loop_over_array('binary_search')
        assert mock_collate.called


def test_set_test_arr_no_dups():
    subject.set_test_arr('binary_search')
    assert subject.test_arr[1] == [1, 2]


def test_set_test_arr_with_dups():
    subject.set_test_arr('find_dups')
    assert subject.test_arr[1] == [2, 2]
