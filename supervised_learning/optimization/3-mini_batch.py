#!/usr/bin/env python3
"""
    Create_mini_batches function
"""

import numpy as np
shuffle_data = __import__('2-shuffle_data').shuffle_data


def create_mini_batches(X, Y, batch_size):
    """
        Creates mini-batches to be used for training a neural network
        using mini-batch gradient descent
    """
    mini_batches = []
    number_of_mb = len(X) // batch_size
    batch_size_copy = batch_size
    i = 0
    X, Y = shuffle_data(X, Y)

    while i in range(len(X)):
        tup = (X[i:batch_size_copy], Y[i: batch_size_copy])
        mini_batches.append(tup)
        i += batch_size
        batch_size_copy += batch_size

    return mini_batches
