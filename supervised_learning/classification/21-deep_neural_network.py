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

        self.__L = len(layers)
        self.__cache = {}
        self.__weights = {}
        for i in range(self.__L):
            self.__weights[f'W{i + 1}'] = np.random.normal(
                size=(layers[i], nx))*(np.sqrt(2 / nx))
            self.__weights[f'b{i + 1}'] = np.zeros((layers[i], 1))
            nx = layers[i]

    @property
    def L(self):
        """
            Getter for L
        """
        return self.__L

    @property
    def cache(self):
        """
            Getter for cache
        """
        return self.__cache

    @property
    def weights(self):
        """
            Getter for weights
        """
        return self.__weights

    def forward_prop(self, X):
        """
            Calculates the forward propagation of a neural network
        """
        self.__cache['A0'] = X
        for i in range(len(self.__weights) // 2):
            z = np.matmul(self.__weights[f'W{i + 1}'], X) + self.__weights[
                f'b{i + 1}']
            A = 1 / (1 + np.exp(-z))
            self.__cache[f'A{i + 1}'] = A
            X = A

        return self.__cache[f'A{len(self.__weights) // 2}'], self.__cache

    def cost(self, Y, A):
        """
            Calculates the cost of the model using logistic regression
        """
        m = len(Y[0])
        return (1 / m) * -(Y * np.log(A) + (1 - Y) * np.log(1.0000001
                                                            - A)).sum()

    def evaluate(self, X, Y):
        """
            Evaluates the neural network's predictions
        """

        A, cache = self.forward_prop(X)
        cost = self.cost(Y, A)
        A = np.where(A > 0.5, 1, 0)

        return A, cost

    def gradient_descent(self, Y, cache, alpha=0.05):
        """
            Calculates one pass of gradient descent on the neural network
        """

        m = len(Y[0])
        weights = self.__weights
        err = cache[f"A{self.L}"] - Y

        for i in range(self.L, 0, -1):
            W, b = f"W{i}", f"b{i}"
            A = f"A{i - 1}"
            bias_gradient = np.sum(err, axis=1, keepdims=True) / m
            Wg = np.matmul(err, cache[A].T) / m
            err = np.matmul(weights[W].T, err)*(cache[A]*(1-cache[A]))
            weights[W] -= alpha * Wg
            weights[b] -= alpha * bias_gradient
