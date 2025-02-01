# Dwie liczby naturalne są ”wspólno-czynnikowe” jeżeli w swoich rozkładach na czynniki pierwsze mają dokładnie jeden wspólny
# czynnik. Na przykład: 24 i 21 albo 32 i 34. Dana jest tablica T[N][N] zawierająca
# liczby naturalne. Dwie liczby w tablicy sąsiadują ze sobą wtedy gdy leżą w tym samym wierszu i sąsiednich
# kolumnach albo leżą w tej samej kolumnie i sąsiednich wierszach. Proszę napisać funkcję four(T), która
# zwraca ilość liczb sąsiadujących z 4 liczbami wspolno-czynnikowymi
import math
def same_factors(x,y):
    count=0
    if x>y:
        for i in range(2, y): # 15 i 27   / 1 i /3
            if x%i==0 and y%i==0 :
                count+=1
        if count ==1:
            return True
    elif x<y:
        for i in range(2, x):
            if x % i == 0 and y % i == 0:
                count += 1
        if count == 1:
            return True
    return False


def find_neighbour(t):
    coordinates=[
        (-1,0),#góra
        (1,0),#dol
        (0,-1),#lewo
        (0,1)#prawo
    ]
    n=len(t)
    general_counter=0

    for i in range(1,n-1):
        for j in range(1, n - 1):
            counter = 0
            for dx,dy in coordinates:
                x,y= i +dx, j +dy
                if same_factors(t[i][j],t[x][y]):
                    counter+=1
            if counter==4: general_counter+=1

    return general_counter

T = [
    [10, 21, 35, 40],
    [18, 15, 12, 49],
    [20, 12, 9, 12],
    [12, 18, 12, 70]
]


print(find_neighbour(T))