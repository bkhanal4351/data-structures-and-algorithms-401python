class LinkedList:
    """
    Create a LinkedList class that includes creates a linked list, insert into the linked list , check existing nodes and insert into a new node if needed.
    """

    def __init__(self):
        self.head = None

    def __str__(self):
        output_str = ''
        current = self.head
        while current:
            output_str += f"{{ {str(current.value)} }} -> "
            current= current.next
        output_str += "NULL"
        return output_str

    def insert(self, value):
        self.head = Node(value, self.head)

    def includes(self, target_value):
        current = self.head

        while current:
            if current.value == target_value:
                return True
            current = current.next
        return False

    def append(self, value):
        new_node = Node(value)
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_before(self, value, new_value):
        if not self.head:
            raise TargetError
        if self.includes(value) is False:
            raise TargetError

        current = self.head

        if current.value == value:
            self.head = Node(new_value, current)
            return
        while current is not None:

            if value == current.next.value:
                current.next = Node(new_value, current.next)
                return
            current = current.next

    def insert_after(self, value, new_value):
        if not self.head:
            raise TargetError
        if self.includes(value) is False:
            raise TargetError

        current = self.head
        while current is not None:

            if value == current.value:
                current.next = Node(new_value, current.next)
                return
            current = current.next

    def kth_from_end(self, k):
        if k < 0:
            raise TargetError
        if self.head is None:
            raise TargetError

        
        length = 0
        current = self.head

        while current:  # this is to traverse to the very end of the list and calculate length
            length += 1
            current = current.next

        if k >= length:
            raise TargetError
        current = self.head
        distance_to_desire_node = length - k  # deducting the input index from user from the length of list returns
        # the expected index value

        while distance_to_desire_node > 1:  # desire node runs the while loop
            current = current.next  # keeps going to the next value until it reaches the desired value
            distance_to_desire_node -= 1  # telling us how many times we have to go to next until we reach the value

        return current.value  # returns expected value


class TargetError(Exception):
    pass


class Node:

    '''
    Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
    '''
    def __init__(self, value, next = None):
        self.next = next
        self.value = value

