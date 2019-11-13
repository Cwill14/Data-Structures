import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll_stack import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # < go left
        # >= go right
        pass

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # to search a give key in Binary Search Tree, we first compare it with root
        # if the key is present at root, we return root. if key is greater than root's key,
        # we recur for right subtree of root node. Otherwise we recur for left subtree.
        pass

    # Return the maximum value found in the tree
    def get_max(self):
        # go right until you can go right no further, then you shall find what you seek
        pass

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        # go left until you can't anymore
        # go back and go right
        # in here somewhere, you want to call cb(node)
        pass

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print In-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
