import pytest
from app import AlgoApp

subject = AlgoApp()


def test_arr_of_1():
    assert subject.graph_arr_generator(1, 1) == [[1]]


def test_2_arrs_limit_2():
    assert subject.graph_arr_generator(2, 2) == [[1], [1, 2]]


def test_limit_5():
    assert subject.graph_arr_generator(5, 5) == [[1], [1, 2], [1, 2, 3], [
        1, 2, 3, 4], [1, 2, 3, 4, 5]]


def test_interval():
    assert subject.graph_arr_generator(5, 10) == [[1, 2], [1, 2, 3, 4], [
        1, 2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
