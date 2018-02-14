#
# Hint: You might need to add more methods to help with traversing the tree
#

import unittest


class Node:
    def __init__(self, val):
        # initializes the value, left child, and right child of the node
        pass

    def getVal(self):
        # Gets the value of the node
        pass

    def setVal(self, val):
        # Sets the value of the node
        pass

    def getChildren(self):
        # Returns the left and right child nodes (if they exist)
        pass


class BinarySearchTree:
    def __init__(self):
        # initializes the root node of the tree
        pass

    def insert(self, val):
        # if the root val is empty, set it
        # otherwise insert a new Node in the correct position (if the value isn't already in the tree)

        pass

    def find(self, val):
        # returns the Node with `val` if it exists
        # otherwise returns none
        pass


class TestBinarySearchTree(unittest.TestCase):

    def test_inserting_new_values_works(self):
        bst = BinarySearchTree()
        self.assertTrue(bst.insert(10))

    def test_duplicates_are_not_inserted(self):
        bst = BinarySearchTree()
        bst.insert(10)
        self.assertFalse(bst.insert(10))

    def test_inserted_node_can_be_found(self):
        bst = BinarySearchTree()
        bst.insert(10)
        self.assertIsNotNone(bst.find(10))

    def test_find_returns_none_for_nonexisting_values(self):
        bst = BinarySearchTree()
        self.assertIsNone(bst.find(10))
        

if __name__ == '__main__':
    unittest.main()
