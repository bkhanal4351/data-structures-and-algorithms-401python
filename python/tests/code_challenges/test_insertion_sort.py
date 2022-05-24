import pytest

from code_challenges.insertion_sort import insertion_sort


def test_insertion_sort():
    lst = [4,6,33,81,19,12]
    actual = insertion_sort(lst)
    expected = [4,6,12,19,33,81]
    assert actual == expected

def test_insertion_sort1():
    lst = [-4,6,33,81,33,12]
    actual = insertion_sort(lst)
    expected = [-4,6,12,33,33,81]
    assert actual == expected


def test_insertion_sort2():
    lst = [-4,6,33,81,19,-12]
    actual = insertion_sort(lst)
    expected = [-12,-4,6,19,33,81]
    assert actual == expected
