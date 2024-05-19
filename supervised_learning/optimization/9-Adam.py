#!/usr/bin/env python3
"""
    Update_variables_Adam function
"""

import numpy as np


def update_variables_Adam(alpha, beta1, beta2, epsilon, var, grad, v, s, t):
    """
        Updates a variable in place using the Adam optimization algorithm
    """

    new_first = beta1 * v + (1 - beta1) * grad
    new_second = beta2 * s + (1 - beta2) * (grad ** 2)

    v_corrected = new_first / (1 - beta1 ** t)
    s_corrected = new_second / (1 - beta2 ** t)

    updated_var = var - (alpha * (v_corrected /
                                  (np.sqrt(s_corrected) + epsilon)))

    return updated_var, new_first, new_second
