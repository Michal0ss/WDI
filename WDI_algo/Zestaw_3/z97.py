#Dane są dwie tablice mogące pomieścić taką samą liczbę elementów: T1[N][N] i T2[M], gdzie M=N*N.
#W każdym wierszu tablicy T1 znajdują się uporządkowane rosnąco (w obrębie wiersza) liczby naturalne.
#Proszę napisać funkcję przepisującą wszystkie singletony (liczby występujące dokładnie raz) z
#tablicy T1 do T2, tak aby liczby w tablicy T2 były uporządkowane rosnąco. Pozostałe elementy tablicy T2
#powinny zawierać zera.

import math
def find_singletons(T1,T2):
    n=len(T1)
    id = [0 for _ in range(n)]
    ind=0
    control=True
    while control:
        control=False
        mini=math.inf
        mini=T1[0][0]
        for i in range(n):
            if mini > T1[i][id]:
                mini = T1[i][id]
        T2[ind]=mini
        ind+=1
        for i in range(n):
            if T1[i][0] == mini and id[i]<n:
                id[i]+=i
                control = True
    return T2