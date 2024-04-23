#!/usr/bin/env python3

import numpy as np

class Node:
    def __init__(self, feature=None, threshold=None, left_child=None, right_child=None, is_root=False, depth=0):
        self.feature = feature
        self.threshold = threshold
        self.left_child = left_child
        self.right_child = right_child
        self.is_leaf = False
        self.is_root = is_root
        self.sub_population = None
        self.depth = depth

    def max_depth_below(self) :

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

class Leaf(Node):
    def __init__(self, value, depth=None):
        super().__init__()
        self.value = value
        self.is_leaf = True
        self.depth = depth

    def max_depth_below(self) :
        return self.depth

class Decision_Tree():
    def __init__(self, max_depth=10, min_pop=1, seed=0, split_criterion="random", root=None):
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

    def depth(self) :
        return self.root.max_depth_below()