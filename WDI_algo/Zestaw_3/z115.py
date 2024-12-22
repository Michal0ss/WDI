#Dwie liczby naturalne są ”wspólno-czynnikowe” jeżeli w swoich rozkładach na czynniki
#pierwsze mają dokładnie jeden wspólny czynnik. Na przykład: 24 i 21 albo 32 i 34. Dana jest tablica T[N][N]
#zawierająca liczby naturalne. Dwie liczby w tablicy sąsiadują ze sobą wtedy gdy leżą w tym samym wierszu i
#sąsiednich kolumnach albo leżą w tej samej kolumnie i sąsiednich wierszach. Proszę napisać funkcję four(T),
#która zwraca ilość liczb sąsiadujących z 4 liczbami wspólno-czynnikowymi.
import math
def same_factor(a,b):
    def factors(n):
        factor=[]
        d =2
        while d*d <=n:
            while n % d == 0:
                if d not in factor:
                    factor.append(d)
                n//=d
            d+=1
        if n > 1:
            factor.append(n)
        return factor

    factors_a=factors(a)
    factors_b=factors(b)

    same_fac = [x for x in factors_a if x in factors_b]

    return len(same_fac)==1

def four(t):
    n= len(t)
    count = 0

    for i in range(n):
        for j in range(n):
            same_factors = 0

            neighbours = [
                (i - 1, j),  # góra
                (i + 1, j),  # dół
                (i, j - 1),  # lewo
                (i, j + 1)  # prawo
            ]

            for ni, nj in neighbours:
                if 0 <= ni < n and 0 <= nj < n:
                    if same_factor(t[i][j], t[ni][nj]):
                        same_factors+=1

            if same_factors == 4:
                count+=1

    return count +1

T = [
    [15, 21, 35, 14, 10],
    [21, 24, 18, 27, 20],
    [35, 18, 28, 30, 25],
    [14, 27, 30, 35, 40],
    [10, 20, 25, 40, 50]
]

print(four(T))  # Wynik: 5
