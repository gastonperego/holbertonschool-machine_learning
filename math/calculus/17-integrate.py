#!/usr/bin/env python3
"""
    poly_integral: Calculates the integral of a polynomial
"""


def poly_integral(poly, C=0):
    """
        Return sa new list of coefficients representing the integral of
        the polynomial
    """
    if not isinstance(C, int) or not isinstance(poly, list) or len(poly) == 0:
        return None
    integral = [C]
    for i in range(len(poly)):
        if poly[i] % (i + 1) == 0: 
            integral.append(int(poly[i] / (i + 1)))
        else:
            integral.append(poly[i] / (i + 1))
    return integral
