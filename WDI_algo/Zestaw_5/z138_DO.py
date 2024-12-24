# ====================================================================================================>
# Zadanie 138
# Dana jest tablica T[N]. Proszę napisać funkcję, która znajdzie niepusty, najmniejszy (w
# sensie liczebności) podzbiór elementów tablicy, dla którego suma elementów jest równa sumie indeksów
# tych elementów. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić sumę elementów znalezionego
# podzbioru. Na przykład dla tablicy: [ 1,7,3,5,11,2 ] rozwiązaniem jest liczba 10.
# ====================================================================================================>


import math

def zadanie_138(t):

    def rek (t, i, s_el=0, s_it=0, best=math.inf, l=0, s_bet=0):
        if i>=len(t):
            return s_el == s_it and s_el > 0, s_el, l