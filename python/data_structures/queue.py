
from data_structures.linked_list import Node
from data_structures.invalid_operation_error import InvalidOperationError


class Queue:
    """
    Put docstring here
    """

    def __init__(self, front = None):
        self.front = front
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = new_node
            self.rear = self.front
            return

        temp = self.rear
        self.rear = new_node
        temp.next = self.rear
        return


    def dequeue(self):
        if self.is_empty():
            raise InvalidOperationError
        old_value = self.front
        self.front = old_value.next
        return old_value.value

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError
        return self.front.value


    def is_empty(self):
        if self.front == None:
            return True
        else:
            False
