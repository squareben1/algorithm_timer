import pytest
from timer import AlgoTimer

subject = AlgoTimer()


def test_arr_of_1():
    assert subject.graph_arr_generator(1, 1) == [[1]]
