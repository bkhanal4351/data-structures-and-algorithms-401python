from data_structures.binary_tree import BinaryTree, Node


class BinarySearchTree(BinaryTree):
    """
    Put docstring here
    """

    def __init__(self):
        self.root = None

    def add(self, value):
        new_node = Node(value)

        def walk(root, new_node):
            if root is None:
                return

            if new_node.value > root.value:
                if root.right:
                    walk(root.right, new_node)
                else:
                    root.right = new_node

            else:
                if root.left:
                    walk(root.left, new_node)
                else:
                    root.left = new_node
        if self.root is None:
            self.root = new_node
            return

        walk(self.root, new_node)



    def contains(self, value):
        if self.root is None:
            return False
        while self.root:
            if self.root.value == value:
                return True
            elif value > self.root.value:
                self.root = self.root.right
            else:
                self.root = self.root.left
        return False

