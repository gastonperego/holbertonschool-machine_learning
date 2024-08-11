#!/usr/bin/env python3
"""
    poly_derivative: Finds the derivative of a polynomial
"""


def poly_derivative(poly):
    """
        Returns a list with the coeficients representing the
        derivative of a polynomial
    """
    if not isinstance(poly, list) or len(poly) == 0:
        return None
    if len(poly) == 1:
        return [0]
    der = []
    for i in range(1, len(poly)):
        der.append(poly[i] * i)
    return der
