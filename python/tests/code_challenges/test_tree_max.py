import pytest
from data_structures.binary_tree import BinaryTree, Node


def test_max_val():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(30)
    tree.root.right = Node(-7)

    actual = tree.find_maximum_value()
    expected = 30

    assert actual == expected


def test_max_val1():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(30)
    tree.root.right = Node(77)

    actual = tree.find_maximum_value()
    expected = 77

    assert actual == expected


def test_max_val2():
    tree = BinaryTree()
    tree.root = Node(100)
    tree.root.left = Node(30)
    tree.root.right = Node(77)
    tree.root.right.right = Node(101)

    actual = tree.find_maximum_value()
    expected = 101

    assert actual == expected


def test_max_val3():
    tree = BinaryTree()
    tree.root = Node(100)
    tree.root.left = Node(30)
    tree.root.right = Node(77)
    tree.root.left.left = Node(101)

    actual = tree.find_maximum_value()
    expected = 101

    assert actual == expected
