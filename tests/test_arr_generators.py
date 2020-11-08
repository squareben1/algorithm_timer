import pytest

from algorithm_timer.arr_generators import *

ten_arr = [[], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [1, 2, 3, 4,
                                                 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]]


def test_confirmation_arr_gen():
    assert arr_generator(2, 10) == [[], [1, 2, 3, 4, 5], [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]


def test_insert_dup():
    assert insert_dup(ten_arr) == [[], [2, 2, 3, 4, 5, 6, 7, 8, 9, 10], [
        2, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 12, 13, 14, 15, 16, 17, 18, 19, 20]]
