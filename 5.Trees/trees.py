""" Tree
Connected, no Cycles, Root, Nodes, Branches, Level, Parent, Child, Leaf, Height, Depth
"""

""" Tree Traversal
1. Depth-First Search
    1.1 Pre-Order
    1.2 In-Order
    1.3 Post-Order
2. Binary Search Tree (Level Order)
"""

"""
Create your own binary tree
"""
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None