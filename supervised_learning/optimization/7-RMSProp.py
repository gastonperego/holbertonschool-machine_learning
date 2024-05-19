#!/usr/bin/env python3
"""
    Create_mini_batches function
"""

import numpy as np


def update_variables_RMSProp(alpha, beta2, epsilon, var, grad, s):
    """
        Updates a variable using the RMSProp optimization algorithm
    """

    new_moment = beta2 * s + (1 - beta2) * (grad ** 2)
    updated_var = var - (alpha * (grad / (np.sqrt(new_moment) + epsilon)))

    return updated_var, new_moment
