#!/usr/bin/env python3
"""
    Neural network class
"""

import numpy as np


class NeuralNetwork:
    """
        Neural network class
    """

    def __init__(self, nx, nodes):
        """
            Init function
        """
        if not isinstance(nx, int):
            raise TypeError('nx must be an integer')
        if nx < 1:
            raise ValueError('nx must be a positive integer')
        if not isinstance(nodes, int):
            raise TypeError('nodes must be an integer')
        if nodes < 1:
            raise ValueError('nodes must be a positive integer')
        self.__W1 = np.random.normal(size=(nodes, nx))
        self.__b1 = np.zeros((nodes, 1))
        self.__A1 = 0
        self.__W2 = np.random.normal(size=(1, nodes))
        self.__b2 = 0
        self.__A2 = 0

    @property
    def W1(self):
        """
            Getter for W1
        """
        return self.__W1

    @property
    def b1(self):
        """
            Getter for b1
        """
        return self.__b1

    @property
    def A1(self):
        """
            Getter for A1
        """
        return self.__A1

    @property
    def W2(self):
        """
            Getter for W2
        """
        return self.__W2

    @property
    def b2(self):
        """
            Getter for b2
        """
        return self.__b2

    @property
    def A2(self):
        """
            Getter for A2
        """
        return self.__A2

    def forward_prop(self, X):
        """
            Calculates the forward propagation of the neural network
        """
        z = np.matmul(self.__W1, X) + self.__b1
        self.__A1 = (1 / (1 + np.exp(-z)))
        z2 = np.matmul(self.__W2, self.__A1) + self.__b2
        self.__A2 = (1 / (1 + np.exp(-z2)))

        return self.__A1, self.__A2

    def cost(self, Y, A):
        """
            Calculates the cost of the model using logistic regression
        """
        m = len(Y[0])
        return (1 / m) * -(Y * np.log(A) + (1 - Y) * np.log(1.0000001
                                                            - A)).sum()

    def evaluate(self, X, Y):
        """
            Evaluates the neural network’s predictions
        """

        A1, A2 = self.forward_prop(X)
        cost = self.cost(Y, A2)

        results = np.where(A2 >= 0.5, 1, 0)
        return results, cost

    def gradient_descent(self, X, Y, A1, A2, alpha=0.05):
        """
            Calculates one pass of gradient descent on the neural network
        """

        m = len(Y[0])
        self.__b1 = self.__b1 - (alpha * ((1 / m) *
                                          ((np.matmul(self.__W2.T,
                                                      (A2 - Y))) *
                                           (A1 * (1 - A1))
                                           ).sum(axis=1, keepdims=True)))
        self.__W1 = self.__W1 - (alpha * ((1 / m) * np.matmul(X,
                                                              (A1 - Y).T)).T)
        self.__b2 = self.__b2 - (alpha * ((1 / m) *
                                          (A2 - Y).sum(axis=1, keepdims=True)))
        self.__W2 = self.__W2 - (alpha * ((1 / m) * np.matmul(A1,
                                                              (A2 - Y).T)).T)
