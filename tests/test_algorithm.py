import pytest
from algorithms import *


class TestFindDups:

    def test_single_item_returns_empty(self):
        assert find_dups([1]) == []


    def test_1_dup_returns_1(self):
        assert find_dups([1, 1]) == [1]


    def test_1_2_2_returns_2(self):
        assert find_dups([1, 2, 2]) == [2]


    def test_doesnt_return_dups(self):
        assert find_dups([1, 2, 2, 2]) == [2]


test_list = [1, 3, 5, 7, 9]

class TestBinarySearch:
    

    def test_binary_search_3(self):
        assert binary_search(test_list, 3) == 1


    def test_binary_search_9(self):
        assert binary_search(test_list, 9) == 4

    