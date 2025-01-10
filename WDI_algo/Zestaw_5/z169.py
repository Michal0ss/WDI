# ====================================================================================================>
# Zadanie 169
# Dwie liczby naturalne są ”wspólno-czynnikowe” jeżeli w swoich rozkładach na czynniki
# pierwsze mają dokładnie jeden wspólny czynnik. Na przykład: 24 i 21 albo 32 i 34.Dana jest tablica T[N][N]
# zawierająca liczby naturalne. Dwie liczby w tablicy sąsiadują ze sobą wtedy gdy leżą w tym samym wierszu i
# sąsiednich kolumnach albo leżą w tej samej kolumnie i sąsiednich wierszach. Proszę napisać funkcję four(T),
# która zwraca ilość liczb sąsiadujących z 4 liczbami wspólno-czynnikowymi.
# ====================================================================================================>
from WDI_algo.Zestaw_5.z168 import first_digit


def czy_wspolno_czynikowe(a, b):
    """
    Dwie liczby są wspólno-czynnikowe, jeśli ich NWD jest liczbą pierwszą.
    """

    def nwd(x, y):
        while y:
            #x, y = y, x % y
            temp = y
            y=x%y
            x = temp
        return x

    def czy_pierwsza(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False

        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    return czy_pierwsza(nwd(a, b))

def rek(t):
    licznik = 0
    directions = ((0, 1), (1, 0), (-1, 0), (0, -1))
    N = len(t)
    for i in range(1, N-1):
        for j in range(1, N-1):
            wspolno_czynnik = 0

            for dx, dy in directions:
                x,y = i+dx, j+dy
                if czy_wspolno_czynikowe(t[i][j], t[x][y]):
                    wspolno_czynnik+=1
            if wspolno_czynnik==4:
                licznik+=1
    return licznik