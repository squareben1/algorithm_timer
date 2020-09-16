import pytest
from algorithms import find_dups


def test_single_item_returns_empty():
    assert find_dups([1]) == []
