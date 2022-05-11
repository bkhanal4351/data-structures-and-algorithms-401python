from queue import Queue

class BinaryTree:
    """
    Put docstring here
    """

    def __init__(self):
      self.root = None

    def pre_order(self):
        ordered_values = []

        def walk(root, values):
            if root is None:
                return

            values.append(root.value)
            walk(root.left, values)
            walk(root.right, values)


        walk(self.root, ordered_values)
        return ordered_values


    def in_order(self):
        ordered_values = []

        def walk(root, values):
            if root is None:
                return


            walk(root.left, values)
            values.append(root.value)
            walk(root.right, values)


        walk(self.root, ordered_values)
        return ordered_values


    def post_order(self):
        ordered_values = []

        def walk(root, values):
            if root is None:
                return


            walk(root.left, values)
            walk(root.right, values)
            values.append(root.value)


        walk(self.root, ordered_values)
        return ordered_values

    def find_maximum_value(self):
        if self.root: # do this when self.root is not None
            value = self.in_order() # set value to call in_order method(we could have used any of the three methods and it would work)
            maximum_value = value[0] # initially set max value to the first index value of the list created in in_order method

            for num in value: # go through for loop and iterate through each number in the list
                if num > maximum_value: # if num is greater than current max value
                    maximum_value = num # reassign max value to num

            return maximum_value #returns max value

        else:
            return False # if self.root is None than return false



# def breadth_first(tree):

#         if tree.root == None:
#             return
#         queue = Queue()
#         queue.enqueue(tree.root)
#         output =[]
#         while not queue.is_empty():
#             front = queue.dequeue()
#             if front.right:
#                 queue.enqueue(front.right)
#             if front.left:
#                 queue.enqueue(front.left)
#             output.append(front.value)
#         return output


class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
