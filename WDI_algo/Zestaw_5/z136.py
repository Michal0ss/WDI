#6. Problem skoczka szachowego. Proszę napisać funkcję, która wypełnia pola szachownicy o
#wymiarach NxN ruchem skoczka szachowe
import time
def jump(t,w,k,i):
    n=len(t)
    dk= (1,2,2,1,-1,-2,-2,-1)
    dw = (-2,-1,1,2,2,1,-1,-2)
    w_n = w+dw[i]
    k_n = k+ dk[i]
    if 0<=w_n < n and 0 <= k_n <n and t[w_n][k_n]==0:
        return(w_n,k_n)
    return -1, -1

def p(t):
    n=len(t)
    for w in range(n):
        for k in range(n):
            print(f"{t[w][k]:3}", end="")
        print()
    print()
    time.sleep(1)

def move(t, w, k, r=1):
    p(t)
    n= len(t)
    t[w][k]=r
    if r == n*n:
        p(t)
    for i in range(8):
        w_n, k_n = jump(t,w,k,i)
        if w_n >=0:
            move(t,w_n,k_n,r+1)
    t[w][k] = 0
        # t[w_n][k_n]=0
n=5
t=[[ 0 for _ in range(n)] for _ in range(n)]
move(t, w=0, k=0)