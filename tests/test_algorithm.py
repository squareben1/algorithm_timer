import pytest
from algorithms import find_dups


def test_single_item_returns_empty():
    assert find_dups([1]) == []


def test_1_dup_returns_1():
    assert find_dups([1, 1]) == [1]


def test_1_2_2_returns_2():
    assert find_dups([1, 2, 2]) == [2]
