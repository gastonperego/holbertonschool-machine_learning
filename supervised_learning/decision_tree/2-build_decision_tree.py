#!/usr/bin/env python3
"""
    Defininig classes
"""

import numpy as np


class Node:
    """
        Node class
    """
    def __init__(self, feature=None, threshold=None,
                 left_child=None, right_child=None, is_root=False, depth=0):
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
            Returns the depth of self tree
        """

        left_depth = 0
        right_depth = 0
        node = self

        while node.right_child:
            right_depth += 1
            node = node.right_child

        while node.left_child:
            left_depth += 1
            node = node.left_child

        if left_depth > right_depth:
            return left_depth
        else:
            return right_depth

    def count_nodes_below(self, only_leaves=False):
        """
            Counts the nodes below a node
        """

        nodes = 1
        leaves = 0
        if self.right_child:
            if not only_leaves:
                nodes += self.right_child.count_nodes_below()
            else:
                leaves += self.right_child.count_nodes_below(only_leaves=True)

        if self.left_child:
            if not only_leaves:
                nodes += self.left_child.count_nodes_below()
            else:
                leaves += self.left_child.count_nodes_below(only_leaves=True)

        if only_leaves:
            if self.is_leaf:
                leaves += 1

        if not only_leaves:
            return nodes
        return leaves

    def __str__(self):
        """
            Prints all the nodes below self
        """

        rigth = self.right_child.right_child_add_prefix(
            self.right_child.__str__())
        left = self.right_child.left_child_add_prefix(
            self.left_child.__str__())

        if self.is_root is True:
            return (f"root [feature={self.feature}, \
threshold={self.threshold}]\n{left}{rigth}")
        else:
            return (f"-> node [feature={self.feature}, \
threshold={self.threshold}]\n{left}{rigth}")

    def left_child_add_prefix(self, text):
        """
            Add prefix to a left child
        """
        lines = text.split("\n")
        new_text = "    +--" + lines[0] + "\n"
        for x in lines[1:]:
            new_text += ("    |  " + x) + "\n"
        return (new_text)

    def right_child_add_prefix(self, text):
        """
            Add prefix to a right child
        """
        lines = text.split("\n")
        new_text = "    +--" + lines[0] + "\n"
        for x in lines[1:]:
            if x != '':
                new_text += ("       " + x) + "\n"
        return (new_text)


class Leaf(Node):
    """
        Class leaf
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
            Returns self.depth
        """
        return self.depth

    def count_nodes_below(self, only_leaves=False):
        """
            Returns 1
        """
        return 1

    def __str__(self):
        """
            Prints a leaf node
        """
        return (f"-> leaf [value={self.value}] ")


class Decision_Tree():
    """
        Class decision tree
    """
    def __init__(self, max_depth=10, min_pop=1, seed=0,
                 split_criterion="random", root=None):
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
            Returns max_depth_below
        """
        return self.root.max_depth_below()

    def count_nodes(self, only_leaves=False):
        """
            Counts the nodes of a tree
        """
        return self.root.count_nodes_below(only_leaves=only_leaves)

    def __str__(self):
        """
            Prints the whole decision tree
        """
        return self.root.__str__()
