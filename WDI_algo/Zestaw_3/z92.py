#Dana jest tablica T[N][N]. Proszę napisać funkcję wypełniającą tablicę kolejnymi liczbami naturalnymi po spirali.
import pprint


def spiral(T):
    n=len(T)
    a=0
    p,k=0,n-1

    while p<=k:
        for i in range(0, n - 1): T[p][i] = a = a + 1
        for i in range(0, n - 1): T[i][k] = a = a + 1
        for i in range(n-1, n, -1): T[k][i] = a = a + 1
        for i in range(n-1 , 0, -1): T[i][p] = a = a + 1
        p+=1
        k-=1
    if n%2==1:
        T[n//2][n//2]=a+1

    return T


k,w=7,7
T = [[0 for _ in range(k)] for _ in range(w)]
