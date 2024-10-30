# Proszę napisać program wczytujący liczbę naturalną i rozkładający ją na iloczyn 2 liczb o
# najmniejszej różnicy. Na przykład: 30 = 5 ∗ 6, 120 = 10 ∗ 12.
# Sprawdzamy czy liczba jest kwadratem
# jesli nie to z wartosci calkowitej pierwastka odejmujemy jeden i sprawdzamy czy dzieli
# i robimy tak dopoki % z tej liczby ==0
# jesli n%i ==0 to dzielimy przez i i printujemy wyniki


import math


def find_min_subtraction(n):
    sqrt_n = int(math.sqrt(n))
    if sqrt_n * sqrt_n == n:
        return sqrt_n

    for i in range(sqrt_n, 0, -1):
        if n % i == 0:
            return i

    return None

n = int(input(" podaj liczbe wieksza od 3"))

if n > 3:
    x= int(find_min_subtraction(n))
    y = int(n / x)
    print(f"{n} = {x} * {y}")
else:
    raise ValueError