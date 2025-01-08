# ====================================================================================================>
# Zadanie 165
# Dana jest tablica T[N] zawierająca liczby naturalne. Proszę napisać funkcję, która odpo-
# wiada na pytanie, czy spośród (niekoniecznie wszystkich) elementów tablicy można utworzyć dwa podzbiory
# o jednakowej sumie elementów, tak aby suma mocy obu podzbiorów wynosiła k. Do funkcji należy przekazać
# wyłącznie tablicę T oraz liczbę naturalną k, funkcja powinna zwrócić wartość typu bool.
# ====================================================================================================>

# n
def zad_165(t,k):
    """Takie zwrocienie true jak tutaj nie konczy funkcji poniewaz zawsze jak po ifie sprawdzamy rekurencyjne wywolanie
    to po prostu wracamy do gornej galezi i sprawdzmay nastepne warunki od nowa a jak sprawdzamy zwykle wartosci
    w instrukcji konca wyjscia to return True zwraca dla calej rekurencji po prostu boolean"""
    def rek(idx, sum1, sum2, size1, size2) -> bool:
        if sum1 == sum2 and size1 + size2 ==4:
            return True

        if idx==len(t):
            return False

        #dodajemy do pierwszego zbioru
        if rek(idx+1, sum1 + t[idx], sum2, size1+1, size2):
            return True         #
        # dodajemy do drugiego
        if rek(idx+1, sum1, sum2+t[idx], size1, size2+1):
            return True
        #pomijamy element
        if rek(idx+1, sum1, sum2, size1, size2):
            return True

        return False
    return rek(0,0,0,0,0)

t = [3, 1, 4, 2, 2]
k = 4
print(zad_165(t, k))


