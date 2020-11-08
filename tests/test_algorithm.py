import pytest
from algorithm_timer.algorithms import *

example_arr = [1, 3, 5, 7, 9]


class TestBinarySearch:

    def test_binary_search_3(self):
        assert binary_search(example_arr, 3) == 1

    def test_binary_search_9(self):
        assert binary_search(example_arr, 9) == 4


class TestLinearSearch:

    def test_linear_search_not_found(self):
        assert linear_search(example_arr, 10) == False

    def test_linear_search_found(self):
        assert linear_search(example_arr, 7) == True


unordered_list = [3, 4, 2, 1, 4, 7]


class TestSelectionSort:

    def test_find_smallest(self):
        assert find_smallest(unordered_list) == 3  # returns smallest index

    def test_selection_sort_ascending(self):
        expected = [1, 2, 3, 4, 4, 7]
        assert selection_sort(unordered_list) == expected


class TestFindDups:

    def test_single_item_returns_empty(self):
        assert find_dups([1]) == []

    def test_1_dup_returns_1(self):
        assert find_dups([1, 1]) == [1]

    def test_1_2_2_returns_2(self):
        assert find_dups([1, 2, 2]) == [2]

    def test_doesnt_return_dups(self):
        assert find_dups([1, 2, 2, 2]) == [2]


uniq_arr = [1, 1, 2]


class TestFindUnique:

    def test_find_uniq(self):
        assert find_uniq(uniq_arr) == [1, 2]


shuffle_arr = [1, 2, 3, 4, 5]
shuffle_arr2 = [1, 2, 3, 4, 5]


class TestShuffle:
    def test_shuffles_arr(self):
        assert slow_shuffle(shuffle_arr) != shuffle_arr

    def test_shuffles_arr_faster(self):
        assert shuffle(shuffle_arr2) != shuffle_arr2
