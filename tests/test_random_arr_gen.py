import pytest

from arr_generators import *


def test_confirmation_arr_gen():
    assert arr_generator(2, 10) == [[], [1, 2, 3, 4, 5], [
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10]]
