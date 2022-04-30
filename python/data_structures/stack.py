from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError


class Stack:
    """
    Put docstring here
    """

    def __init__(self, top = None):
        self.top = None

    def push(self, value):
       self.top = Node(value, self.top)

    def pop(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        old_value = self.top
        self.top = self.top.next
        old_value.next = None
        return old_value.value

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.top.value



    def is_empty(self):
        return self.top == None
