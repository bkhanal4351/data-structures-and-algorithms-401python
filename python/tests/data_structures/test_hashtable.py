import pytest
from data_structures.hashtable import Hashtable



def test_exists():
    assert Hashtable

def test_create_default():
    ht = Hashtable()
    actual = ht.size
    expected = 1024
    assert actual == expected

def test_hash():
    """
    hash
Arguments: key
Returns: Index in the collection for that key
    """
    ht = Hashtable()
    index = ht.hash("cat")
    assert 0 <= index < ht.size



def test_get_apple1():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected

def test_set_apple():
    ht = Hashtable()
    ht.set('fruit', 'apple')
    fruit_index = ht.hash('fruit')
    actual = ht.buckets[fruit_index]
    expected = ('fruit','apple')
    assert actual.head.value == expected

def test_contains():
    ht = Hashtable()
    ht.set('movie', 'primer')
    expected = True
    actual = ht.contains('movie')
    assert actual == expected

def test_get_apple():
    ht = Hashtable()
    ht.set("fruit", "apple")
    actual = ht.get("fruit")
    expected = "apple"
    assert actual == expected


def test_collisions():
    ht = Hashtable()
    ht.set("cat", "Josie")
    ht.set("act", "A Contemporary Theater")
    ht.set("tac", "Taco Tuesday")

    assert ht.get("cat") == "Josie"
    assert ht.get("act") == "A Contemporary Theater"
    assert ht.get("tac") == "Taco Tuesday"

@pytest.mark.skip("TODO")
def test_internals():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")

    actual = []

    # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
    for item in hashtable.buckets:
        if item:
            actual.append(item.display())

    expected = [[["silent", True], ["listen", "to me"]], [["ahmad", 30]]]

    assert actual == expected
