#  Proszę napisać program wyznaczający pierwiastek kwadratowy ze wzoru Newtona.
# an+1 = (r/an + an)/2
from math import sqrt
def newton_sqrt(n, tolerance = 1e-6):

    x = sqrt(n)

    while True:
        # Obliczenie kolejnego przybliżenia
        next_x = (n/x+x)/2.0

        if abs(next_x - x) < tolerance:
            return next_x

        x = next_x # aktualizacja


n = 10
result = newton_sqrt(n)
print(f"{n}: {result}")