#!/usr/bin/env python3
"""
    l2 cost function
"""

import numpy as np


def l2_reg_cost(cost, lambtha, weights, L, m):
    """
        Calculates the cost of a neural network after l2 regularization
    """
    sum = 0
    for i in range(1, L + 1):
        sum += (weights[f'W{i}'] ** 2).sum()

    return cost + (lambtha / (2 * m)) * sum
