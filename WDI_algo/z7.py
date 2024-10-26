#  Proszę zmodyfikować wzór Newtona aby program z poprzedniego zadania obliczał pierwiastek
# stopnia 3.

from math import sqrt
def newton(n, tolerance = 1e-10):
    x=n/2.0

    while True:
        next_x = (2*x+n/(x**2))/3.0

        if abs(next_x - x)<tolerance:
            return next_x

        x = next_x

n = 10
result = newton(n)
print(f"{n}: {result}")