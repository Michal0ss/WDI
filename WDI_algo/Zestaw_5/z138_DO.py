# ====================================================================================================>
# Zadanie 138
# Dana jest tablica T[N]. Proszę napisać funkcję, która znajdzie niepusty, najmniejszy (w
# sensie liczebności) podzbiór elementów tablicy, dla którego suma elementów jest równa sumie indeksów
# tych elementów. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić sumę elementów znalezionego
# podzbioru. Na przykład dla tablicy: [ 1,7,3,5,11,2 ] rozwiązaniem jest liczba 10.
# ====================================================================================================>


import math

def zadanie_138(t):

    def rek (t, idx, sum_el, sum_idx, el_amount_subseq = 0, optimal_sum=0):
        if idx >= len(t):
            return sum_el==sum_idx and sum_el>0

    sum_best = 0
    poss = False


