#!/usr/bin/env python3
"""
    sumation_i_squared: calculates the summatory of i = 1, i^2 with n as
    stoppping condition
"""


def summation_i_squared(n):
    """
        Calculates the summatory of i^2 with i starting at 1 until n
    """
    if not isinstance(n, int) or n < 1:
        return None
    return int((n * (n + 1) * ((2 * n) + 1)) / 6)

