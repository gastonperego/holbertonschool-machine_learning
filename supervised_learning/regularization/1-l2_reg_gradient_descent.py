#!/usr/bin/env python3
"""
    l2 cost function
"""

import numpy as np


def l2_reg_gradient_descent(Y, weights, cache, alpha, lambtha, L):
    """
        Updates the weights and biases of a neural network using gradient
        descent with L2 regularization
    """
    m = Y.shape[1]
    dZ = cache[f'A{L}'] - Y
    for low in range(L, 0, -1):
        A_prev = cache[f'A{low-1}']
        W = weights[f'W{low}']
        dW = 1/m * np.dot(dZ, A_prev.T) + (lambtha/m)*W
        db = 1/m * np.sum(dZ, axis=1, keepdims=True)
        dZ = np.dot(W.T, dZ) * (1 - np.power(A_prev, 2))
        weights[f'W{low}'] -= alpha * dW
        weights[f'b{low}'] -= alpha * db
