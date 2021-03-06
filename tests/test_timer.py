import pytest
# from time import sleep
import time

from algorithm_timer.timer import AlgoTimer

subject = AlgoTimer()
input_arr = [1, 2, 3]


def return_after_point_one_sec(arr):
    time.sleep(0.1)
    return arr


@pytest.mark.skip("Slow test")
def test_basic_timer():
    output = subject.basic_timer(return_after_point_one_sec, input_arr)
    assert output > 0.1 and output < 0.15


@pytest.mark.skip("Slow test")
def test_get_average():
    output = subject.get_average(return_after_point_one_sec, input_arr)
    assert output[0] > 0.1 and output[0] < 0.15
    assert output[1] == 3
