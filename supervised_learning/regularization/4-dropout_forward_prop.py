#!/usr/bin/env python3
"""
    Dropout forward prop function
"""

import numpy as np


def dropout_forward_prop(X, weights, L, keep_prob):
    cache = {}
    cache['A0'] = X
    for i in range(1, L + 1):
        Z = np.matmul(weights[f'W{i}'], cache[f'A{i - 1}']) + weights[f'b{i}']
        if i == L:
            t = np.exp(Z)
            A = t / np.sum(t, axis=0, keepdims=True)
        else:
            A = np.tanh(Z)
            D = np.random.rand(A.shape[0], A.shape[1]) < keep_prob
            A *= D
            A /= keep_prob
            cache[f'D{i}'] = D
        cache[f'A{i}'] = A
    return cache
