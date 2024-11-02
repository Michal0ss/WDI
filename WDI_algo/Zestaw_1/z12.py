# Proszę napisać program wypisujący rozkład liczby na czynniki pierwsze
from math import sqrt

def divide_till_non(n):
    divider = 2

    # Sprawdzamy wszystkie liczby, zaczynając od 2
    while divider**2 <= n:
        # Jeśli dzielnik jest czynnikiem, wypisujemy go i dzielimy n
        while  n % divider == 0:
            print(divider, end=" ")
            n //=divider
        divider+=1

    if n>=1:
        print(n)

n = int(input("Podaj liczbę do rozkładu na czynniki pierwsze: "))
print(f"Czynniki pierwsze liczby {n}: ", end=" ")
divide_till_non(n)
print()


