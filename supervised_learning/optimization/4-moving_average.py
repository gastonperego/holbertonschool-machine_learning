#!/usr/bin/env python3
"""
    Moving_average function
"""

import numpy as np


def moving_average(data, beta):
    """
        Calculates the weighted moving average of a data set:
    """
    results = []
    v = 0

    for i in range(len(data)):
        v = beta * v + (1 - beta) * data[i]
        result = v / (1 - beta ** (i + 1))
        results.append(result)

    return results
