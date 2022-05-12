from data_structures.binary_tree import BinaryTree, Node
from data_structures.queue import Queue


# class BinaryTree:
#     def __init__(self, root=None, values=None):
#         self.root = root
#         if values:
#             for value in values:
#                 self.add(value)

#     def add(self, value):

#         node = Node(value)

#         if not self.root:
#             self.root = node
#             return

#         breadth = Queue()

#         breadth.enqueue(self.root)

#         while not breadth.is_empty():
#             front = breadth.dequeue()
#             if not front.left:
#                 front.left = node
#                 return
#             else:
#                 breadth.enqueue(front.left)

#             if not front.right:
#                 front.right = node
#                 return
#             else:
#                 breadth.enqueue(front.right)


def breadth_first(tree):
    queue = Queue() # calling queue method
    queue.enqueue(tree.root) # enqueue root
    output = [] # set output as empty string

    if tree.root is None: # base case if root is none than return empty list
        return output

    while not queue.is_empty(): # white queue is not empty
        front = queue.dequeue() # set front equals to dequeue
        output.append(front.value) # append front value to output
        if front.left: # if left is not empty
            queue.enqueue(front.left) # enqueue to left

        if front.right: # if right is not empty
            queue.enqueue(front.right) # enqueue to right

    return output # return output list
