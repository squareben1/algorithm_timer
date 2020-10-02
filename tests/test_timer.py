import pytest
# from time import sleep
import time

from timer import AlgoTimer

subject = AlgoTimer()
input_arr = [1,2,3]

def return_after_point_one_sec(arr):
    time.sleep(0.1)
    return arr

def test_basic_timer():
    output = subject.basic_timer(return_after_point_one_sec, input_arr)
    print(output)
    assert output > 0.1 and output < 0.2