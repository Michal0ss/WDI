# Proszę napisać program obliczający wartości cos(x) z rozwinięcia w szereg Maclaurina.

import math


def maclaurin_cos(x, terms):
    """
       Calculate cosine using Maclaurin series expansion without using math.factorial.

       :param x: Value to calculate cos(x) for.
       :param terms: Number of terms to include in the expansion.
       :return: Approximation of cos(x) by Maclaurin series.
       :variable term: is q in sequence
       """
    cosx=0
    term = 1
    #term = ((-1) ** n * x ** (2*n))/(math.factorial(2*n))
    for n in range(terms):
        term *= -x ** 2 / ((2 * n - 1) * (2 * n)) #cosx += ((-1) ** n * x ** (2 * n)) / (math.factorial(2 * n))
        cosx += term  #  ! -> wersja bez biblioteki math i term to jest q ciagu !!
    return cosx

x_value = math.pi / 3

approx_cosx = maclaurin_cos(x_value, terms=4)
print(f"Approximation of cos({x_value}) using Maclaurin series: {approx_cosx}")
print(f"Actual value of cos({x_value}): {math.cos(x_value)}")
