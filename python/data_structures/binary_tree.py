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

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
