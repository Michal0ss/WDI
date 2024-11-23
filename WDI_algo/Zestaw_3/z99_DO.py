# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
# w poszukuje w tablicy najdłuższego ciągu geometrycznego leżącego ukośnie w kierunku prawo-dół, liczącego
# co najmniej 3 elementy. Do funkcji należy przekazać tablicę. Funkcja powinna zwrócić informacje czy udało
# się znaleźć taki ciąg oraz długość tego ciągu

import math
def find_seq(t):
    max_len=0
    n=len(t)
    q=[]
    for i in range(1, n+1):
        d=t[i-1][i-1]//t[i][i]
        q.append(d)
        if q[i-1] == q[i]:
            max_len+=1
        else:
            max_len=0
    if max_len==3:
        return max_len

T = [
    [1, 2, 3, 4],
    [2, 1, 6, 8],
    [3, 6, 2, 12],
    [4, 8, 16, 4]
]
print(find_seq(T))