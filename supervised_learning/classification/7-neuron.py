#!/usr/bin/env python3
"""
    Neuron class
"""

import numpy as np
import matplotlib.pyplot as plt


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

    def forward_prop(self, X):
        """
            Calculates the forward propagation of a neuron
        """

        matrix = np.matmul(self.__W, X) + self.__b
        result = (1 / (1 + np.exp(-matrix)))
        self.__A = result
        return result

    def cost(self, Y, A):
        """
            Calculates the cost of the neuron using logistic regression
        """
        m = len(Y[0])
        return (1 / m) * -(Y * np.log(A) + (1 - Y) * np.log(1.0000001
                                                            - A)).sum()

    def evaluate(self, X, Y):
        """
            Evaluates the predictions of the neuron
        """

        results = self.forward_prop(X)
        cost = self.cost(Y, results)

        results = np.where(results >= 0.5, 1, 0)

        return results, cost

    def gradient_descent(self, X, Y, A, alpha=0.05):
        """
            Calculates one pass of gradient descent on the neuron
        """
        m = len(Y[0])
        self.__b = self.__b - (alpha * ((1 / m) * (A - Y).sum()))
        self.__W = self.__W - (alpha * ((1 / m) * np.matmul(X, (A - Y).T)).T)

    def train(self, X, Y, iterations=5000, alpha=0.05,
              verbose=True, graph=True, step=100):
        """
            Trains the neuron the iteration times
        """
        if not isinstance(iterations, int):
            raise TypeError('iterations must be an integer')
        if iterations < 0:
            raise ValueError('iterations must be a positive integer')
        if not isinstance(alpha, float):
            raise TypeError('alpha must be a float')
        if alpha < 0:
            raise ValueError('alpha must be positive')
        if verbose is True or graph is True:
            if not isinstance(step, int):
                raise TypeError('step must be an integer')
            if step < 0 or step > iterations:
                raise ValueError('step must be positive and <= iterations')

        self.__A = self.forward_prop(X)
        step_copy = step
        costs = []
        cost = self.cost(Y, self.__A)
        print(f"Cost after 0 iterations: {cost}")
        for i in range(iterations + 1):
            self.gradient_descent(X, Y, self.__A, alpha)
            if verbose is True and i == step_copy:
                print(f"Cost after {i} iterations: {self.cost(Y, self.__A)}")
                step_copy += step
            if graph is True:
                costs.append(self.cost(Y, self.__A))
            self.__A = self.forward_prop(X)
        if graph is True:
            plt.scatter(np.arange(0, iterations + 1), np.array(costs))
            plt.title('Training Cost')
            plt.xlabel('iteration')
            plt.ylabel('cost')
            plt.show()

        return self.evaluate(X, Y)
