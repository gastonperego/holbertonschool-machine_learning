#!/usr/bin/env python3
"""
    Deep neural network class
"""

import numpy as np


class DeepNeuralNetwork:
    """
        Deep neural network class
    """

    def __init__(self, nx, layers):
        """
            Init function
        """

        if not isinstance(nx, int):
            raise TypeError('nx must be an integer')
        if nx < 1:
            raise ValueError('nx must be a positive integer')
        if not isinstance(layers, list) or len(layers) == 0:
            raise TypeError('layers must be a list of positive integers')
        if not all(map(lambda n: isinstance(n, int) and n > 0, layers)):
            raise TypeError('layers must be a list of positive integers')

        self.L = len(layers)
        self.cache = {}
        self.weights = {}
        for i in range(self.L):
            self.weights[f'W{i + 1}'] = np.random.normal(size=(layers[i], nx)
                                                         )*(np.sqrt(2 / nx))
            self.weights[f'b{i + 1}'] = np.zeros((layers[i], 1))
            nx = layers[i]
