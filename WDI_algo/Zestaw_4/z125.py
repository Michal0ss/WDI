# ====================================================================================================>
# Zadanie 125
# Liczby zespolone są reprezentowane przez krotkę(re,im).
# Gdzie:re-część rzeczywista liczby,im-częśćurojonaliczby.
# Proszę napisać podstawowe operacje na liczbach zespolonych ,m.in.dodawanie,
# odejmowanie, mnożenie, dzielenie, potęgowanie, wypisywanie i wczytywanie.
# ====================================================================================================>


def dodawanie(c1, c2):
    return c1[0] + c2[0], c1[1] + c2[1]

def odejmowanie(c1, c2):
    return c1[0]-c2[0], c1[1]-c2[1]

def mnozenie(c1, c2):
    return c1[0]*c2[0]- c1[1]*c2[1], c1[0]*c2[1] + c2[0]*c1[1]

def dzielenie(c1, c2): # c1/c2
    a,b = c2
    sprzezeniec2= (a,-b)
    licznik = mnozenie(c2, sprzezeniec2)
    mianownik = a**2 + b**2
    re,im = licznik
    return re / mianownik, im/mianownik


def potegowanie(c1, n):
    re,im=c1
    wynik_re = 1
    wynik_im = 0
    for _ in range(n):
        wynik_re, wynik_im = mnozenie((wynik_re, wynik_im), (re,im))
    return wynik_re, wynik_im

