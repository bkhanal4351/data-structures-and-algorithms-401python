import pytest
from code_challenges.when_in_rome import when_in_rome


def test_rome_num():
    roman = 'VI'
    actual = when_in_rome(roman)
    expected = 6
    assert actual == expected

def test_rome_num1():
    roman = 'IV'
    actual = when_in_rome(roman)
    expected = 4
    assert actual == expected

def test_rome_num2():
    roman = 'VIII'
    actual = when_in_rome(roman)
    expected = 8
    assert actual == expected

def test_rome_num3():
    roman = 'MC'
    actual = when_in_rome(roman)
    expected = 1100
    assert actual == expected

def test_rome_num4():
    roman = 'CM'
    actual = when_in_rome(roman)
    expected = 900
    assert actual == expected

def test_rome_num5():
    roman = 'CMI'
    actual = when_in_rome(roman)
    expected = 901
    assert actual == expected

def test_rome_num6():
    roman = 'CMIX'
    actual = when_in_rome(roman)
    expected = 909
    assert actual == expected

def test_rome_num7():
    roman = 'CMXVI'
    actual = when_in_rome(roman)
    expected = 916
    assert actual == expected
def test_rome_num8():
    roman = 'cMXVI'
    actual = when_in_rome(roman)
    expected = 916
    assert actual == expected

def test_rome_num9():
    roman = 'vii'
    actual = when_in_rome(roman)
    expected = 7
    assert actual == expected

