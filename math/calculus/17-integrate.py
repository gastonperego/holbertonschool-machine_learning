#!/usr/bin/env python3
"""
    Task 17
"""


def poly_integral(poly, C=0):
    """
        Calculates the integral of a polynomial
    """

    integral = [C]
    if not isinstance(poly, list) or not isinstance(C, int) or len(poly) == 0:
        return None
    i = len(poly) - 1

    while i >= 0 and poly[i] == 0:
        poly.pop(i)
        i -= 1

    for i in range(len(poly)):
        if poly[i] % (i + 1) == 0:
            integral.append(int(poly[i] / (i + 1)))
        else:
            integral.append(poly[i] / (i + 1))

    return integral
