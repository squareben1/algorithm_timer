import pytest
from timer import AlgoTimer

subject = AlgoTimer()


def test_arr_of_1():
    assert subject.graph_arr_generator(1, 1) == [[1]]


def test_2_arrs_limit_2():
    assert subject.graph_arr_generator(1, 2) == [[1], [1, 2]]


def test_limit_5():
    assert subject.graph_arr_generator(1, 5) == [[1], [1, 2], [1, 2, 3], [
        1, 2, 3, 4], [1, 2, 3, 4, 5]]
