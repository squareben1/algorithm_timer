import pytest

from app import AlgoApp

subject = AlgoApp(10, 5)


def test_slice_outlier_results():
    arr_input = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected = [2, 3, 4, 5, 6, 7, 8, 9]
    assert subject.slice_outlier_results(arr_input) == expected
