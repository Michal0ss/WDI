# Dane są ciągi: An+1 = sqrt(An ∗ Bn) oraz Bn+1 = (An + Bn)/2.0.
# Ciągi te są zbieżne do wspólnej granicy nazywanej średnią arytmetyczno-geometryczną.
# Proszę napisać program wyznaczający średnią
# arytmetyczno-geometryczną dwóch liczb naturalnych.

import math

def a_geo(a,b,tolerance=1e-10):
    an = a
    bn = b

    while abs(an-bn) > tolerance:
        an_next = math.sqrt(an*bn)
        bn_next = (an+bn)/2.0

        an, bn = an_next, bn_next

    return an, bn

print(a_geo(24,6))