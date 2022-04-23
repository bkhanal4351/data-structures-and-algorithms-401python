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


class TargetError:
    pass


class Node:

    '''
    Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
    '''
    def __init__(self, value, next = None):
        self.next = next
        self.value = value

