#!/usr/bin/env python3
"""
    Task 0
"""
import numpy as np
import matplotlib.pyplot as plt


def line():
    """
        Creates a graphic of the number from 0 to 10 to the power of 3
    """

    y = np.arange(0, 11) ** 3
    plt.figure(figsize=(6.4, 4.8))

    plt.plot(y, color="r")
    plt.xlim(0, 10)
    plt.show()
