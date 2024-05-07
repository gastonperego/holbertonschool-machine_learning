#!/usr/bin/env python3
"""
    One hot decode function
"""

import numpy as np


def one_hot_decode(one_hot):
    """
        Converts a one-hot matrix into a vector of labels
    """
    try:
        if not isinstance(one_hot, np.ndarray):
            return None
        labels = []
        for line in one_hot.T:
            for i in range(len(line)):
                if line[i] == 0:
                    continue
                else:
                    labels.append(i)
                    break
        return np.array(labels)
    except:
        return None
