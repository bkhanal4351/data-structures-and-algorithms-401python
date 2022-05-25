import pytest
from code_challenges.merge_sort import merge_sort

def test_merge_sort():
    lst = [3,9,6,15]
    actual = merge_sort(lst)
    expected = [3,6,9,15]
    assert actual == expected

def test_merge_sort1():
    lst = [3,9,6,16,-15]
    actual = merge_sort(lst)
    expected = [-15,3,6,9,16]
    assert actual == expected

def test_merge_sort2():
    lst = [10,9,8,7,6,5,4,3,2,1]
    actual = merge_sort(lst)
    expected = [1,2,3,4,5,6,7,8,9,10]
    assert actual == expected
