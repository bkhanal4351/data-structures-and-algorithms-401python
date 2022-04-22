class LinkedList:
    """
    Put docstring here
    """

    def __init__(self):
        self.head = None

    # def __str__(self):


    def insert(self, value):
        self.head = Node(value, self.head)

    def includes(self, target_value):
        current = self.head

        while current:
            if current.value == target_value:
                return True
            current == current.next
        return False


class TargetError:
    pass


class Node:
    def __init__(self, value, next = None):
        self.next = next
        self.value = value

