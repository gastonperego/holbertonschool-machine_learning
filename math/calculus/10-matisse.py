#!/usr/bin/env python3
"""
    Task 10
"""


def poly_derivative(poly):
    """
        Calculates the derivative of a polynomial
    """

    if not isinstance(poly, list) or len(poly) == 0:
        return None

    if len(poly) == 1:
        return [0]

    i = 1
    der = []

    while i <= len(poly) - 1:
        der.append((poly[i] * i))
        i += 1

    return der
