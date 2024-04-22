#!/usr/bin/env python3
"""
    Task 9
"""


def summation_i_squared(n):
    """
        Calculates the summation of i^2 with i starting at 1 and stopping at n
    """

    if not isinstance(n, int) or n < 1:
        return None

    return int((n * (n + 1) * ((2 * n) + 1)) / 6)
