# ====================================================================================================>
# Zadanie 126
# Używając funkcji z poprzedniego zadania proszę napisać funkcję rozwiązującą równanie
# kwadratowe o współczynnikach zespolonych.
# ====================================================================================================>

def dodawanie(c1, c2):
    return c1[0] + c2[0], c1[1] + c2[1]


def odejmowanie(c1, c2):
    return c1[0] - c2[0], c1[1] - c2[1]


def mnozenie(c1, c2):
    return c1[0] * c2[0] - c1[1] * c2[1], c1[0] * c2[1] + c1[1] * c2[0]

def dzielenie(c1, c2):
    re2, im2 = c2
    sprzegenie_c2 = (re2, -im2)
    licznik = mnozenie(c1, sprzegenie_c2)
    mianownik = re2**2 + im2**2
    re, im = licznik
    return re / mianownik, im / mianownik


def potegowanie(c1, n):
    re, im = c1
    wynik_re = 1
    wynik_im = 0
    for _ in range(n):
        wynik_re, wynik_im = mnozenie((wynik_re, wynik_im), (re, im))
    return wynik_re, wynik_im

def Zadanie_126(a, b, c):...