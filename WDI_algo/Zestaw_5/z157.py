# ====================================================================================================>
# Zadanie 157
# Tablica T =[(x1,y1),(x1,y1),...] zawiera położenia N punktów o współrzędnych opisanych
# wartościami typu float .Proszę napisać funkcję, która zwróci najmniejszą odległość między środkami ciężkości
# 2 niepustych podzbiorów tego zbioru.
# ====================================================================================================>

import math
from turtledemo.penrose import inflatedart


def srodek_ciezkosci(subseq):
    """suma kazdego x i suma kazdego y podzielona przez ilosc wspolrzednych"""
    liczba_pkt = len(subseq)
    sum_x = sum(p[0] for p in subseq)
    sum_y = sum(p[1] for p in subseq)
    return sum_x // liczba_pkt, sum_y // liczba_pkt

def oblicz_odleglosci(p1,p2):
    """odleglosc miedzy dwoma punktami z analitycznej"""
    return math.sqrt((p2[0]-p1[0])**2 + (p2[1]-p1[1])**2)

def generuj_podzbiory(t):
    """
    Generuje wszystkie możliwe podzbiory rekurencyjnie, dodając podzbiory z pierwszym
    elementem i bez pierwszego elementu tablicy, aż do dotarcia do końca tablicy.
    """
    if t == []:
        return [[]]

    subseq = generuj_podzbiory(t[1:])

    subseq_w_first = [[t[0]] + sub for sub in subseq]

    return subseq + subseq_w_first

def zad_157(t):
    """
    Dla każdego, poza pustym, podzbiorem generuje środki ciężkości.
    Wszystkie środki ciężkości są porównywane, a następnie wyszukiwana jest najmniejsza różnica.
    """

    subseq = generuj_podzbiory(t)

    subseq_wo_empty = subseq[1:]
    srodki_ciezkosci = [srodek_ciezkosci(p) for p in subseq_wo_empty]

    min_len = math.inf
    for i in range(len(srodki_ciezkosci)):
        for j in range(i+1, len(srodki_ciezkosci)):
            odlgelosc  = oblicz_odleglosci(srodki_ciezkosci[i], srodki_ciezkosci[j])
            min_len = min(min_len, odlgelosc)

    return min_len