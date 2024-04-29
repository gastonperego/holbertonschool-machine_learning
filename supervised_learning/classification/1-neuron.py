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

        self.__W = np.random.normal(size=(1, nx))
        self.__b = 0
        self.__A = 0

    @property
    def W(self):
        """
            Geeter for W
        """
        return self.__W

    @property
    def b(self):
        """
            Geeter for b
        """
        return self.__b

    @property
    def A(self):
        """
            Geeter for A
        """
        return self.__A
