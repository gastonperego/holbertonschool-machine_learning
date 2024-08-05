#!/usr/bin/env python3
"""
    scatter: Plots a linaear function
"""
import numpy as np
import matplotlib.pyplot as plt


def scatter():
    """
        Plots x -> y as scatter plot
    """
    mean = [69, 0]
    cov = [[15, 8], [8, 15]]
    np.random.seed(5)
    x, y = np.random.multivariate_normal(mean, cov, 2000).T
    y += 180
    plt.figure(figsize=(6.4, 4.8))

    plt.scatter(x, y, c='m', marker='.')
    plt.savefig('plot.png')
    plt.show()
