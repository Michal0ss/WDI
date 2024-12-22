# Liczby wymierne są reprezentowane przez krotkę (l,m). Gdzie: l - liczba całkowita oznaczająca licznik,
# m - liczba naturalna oznaczająca mianownik. Proszę napisać podstawowe operacje na ułamkach,
# m.in. dodawanie, odejmowanie, mnożenie, dzielenie, potęgowanie, skracanie, wypisywanie i wczytywanie.
from typing import Tuple

def sums(x,y: Tuple[int, int]) -> tuple:
    l, m = x[0], x[1]
    l1, m1 = y[0], y[1]
    if m== m1:
        return l + l1, m
    else:
        return l*m1 + l1*m, m*m1

def subtraction(x,y: Tuple[int, int]) -> tuple:
    l, m = x[0], x[1]
    l1, m1 = y[0], y[1]
    if m== m1:
        return l - l1, m
    else:
        return l*m1 - l1*m, m*m1

def multiply(x,y: Tuple[int, int]) -> tuple:
    l, m = x[0], x[1]
    l1, m1 = y[0], y[1]
    return l*l1, m*m1

def divide(x,y: Tuple[int, int]) -> tuple:
    l, m = x[0], x[1]
    l1, m1 = y[0], y[1]
    return l*m1, m*l1

def power(x: Tuple[int], p) -> tuple:
    l, m = x[0], x[1]
    return l**p, m**p

def nwd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def reduction(x: Tuple[int]) -> tuple:
    l, m = x[0], x[1]
    x = nwd(l,m)
    return l//x,m//x
