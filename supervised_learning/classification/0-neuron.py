#!/usr/bin/env python3
"""
    Neuron class
"""

import numpy as np


class Neuron:
    """
        Neuron class
    """

    def __init__(self, nx):
        """
            Init function
        """
        if not isinstance(nx, int):
            raise TypeError('nx must be an integer')
        elif nx < 1:
            raise ValueError('nx must be a positive integer')

        self.W = np.random.normal(size=(1, nx))
        self.b = 0
        self.A = 0
