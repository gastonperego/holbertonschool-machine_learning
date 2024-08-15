#!/usr/bin/env python3
"""
    Class Node: It is the class that represents a node of the tree.

    - max_depth_below: returns the max depth below that node

    Class Leaf: It is the class that represents a leaf of a tree

    - max_depth_below: Returns the depth of the leaf (self.depth)

    Class DecisionTree: It is very similar to the node class, but this node
    is the root of the tree
"""

import numpy as np


class Node:
    """
        Node class
    """
    def __init__(self, feature=None, threshold=None, left_child=None,
                 right_child=None, is_root=False, depth=0):
        """
            Init function
        """
        self.feature = feature
        self.threshold = threshold
        self.left_child = left_child
        self.right_child = right_child
        self.is_leaf = False
        self.is_root = is_root
        self.sub_population = None
        self.depth = depth

    def max_depth_below(self):
        """
            Returns the depth below the given node
        """
        if self.is_leaf:
            return self.depth
        right = self.right_child.max_depth_below()
        left = self.left_child.max_depth_below()

        return max(right, left)

    def count_nodes_below(self, only_leaves=False):
        """
            Counts the nodes below this node, with the option to count
            only the leaves
        """
        size = 0
        if only_leaves:
            size += (self.right_child.count_nodes_below(only_leaves=True) +
                     self.left_child.count_nodes_below(only_leaves=True))
            return size
        size += (self.right_child.count_nodes_below() +
                 self.left_child.count_nodes_below())

        return size + 1


class Leaf(Node):
    """
        Leaf class
    """
    def __init__(self, value, depth=None):
        """
            Init function
        """
        super().__init__()
        self.value = value
        self.is_leaf = True
        self.depth = depth

    def max_depth_below(self):
        """
            Returns the depth of the leaf
        """
        return self.depth

    def count_nodes_below(self, only_leaves=False):
        """
            Returns 1
        """
        return 1


class Decision_Tree():
    """
        Decision_Tree class
    """
    def __init__(self, max_depth=10, min_pop=1,
                 seed=0, split_criterion="random", root=None):
        """
            Init function
        """
        self.rng = np.random.default_rng(seed)
        if root:
            self.root = root
        else:
            self.root = Node(is_root=True)
        self.explanatory = None
        self.target = None
        self.max_depth = max_depth
        self.min_pop = min_pop
        self.split_criterion = split_criterion
        self.predict = None

    def depth(self):
        """
            Returns the depth of the tree
        """
        return self.root.max_depth_below()

    def count_nodes(self, only_leaves=False):
        """
            Returns the number of nodes of the tree, with the option to
            exclude the root and the internal nodes (only return the ammount
            of leaves)
        """
        return self.root.count_nodes_below(only_leaves=only_leaves)
