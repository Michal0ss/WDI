# Na szachownicy o wymiarach N × N umieszczono pewną liczbę pionków.
# Położenie pionków opisuje lista [(w0, k0),(w1, k1),(w2, k2), ...].
# W lewym górnym rogu szachownicy (o współrzędnych 0, 0) znajduje się
# król, który musi dotrzeć do prawego dolnego rogu szachownicy. Król może wykonywać ruchy w prawo, w
# dół lub w górę szachownicy, nie może zbijać pionków ani wracać na pole, na którym już był. Proszę napisać
# funkcję king(N,L), która zwróci maksymalną liczbę ruchów jakie może wykonać król na drodze do celu. Do
# funkcji należy przekazać wyłącznie dwa parametry: rozmiar szachownicy N oraz listę L zawierającą położenia pionków.
# Jeżeli dotarcie do celu nie jest możliwe funkcja powinna zwrócić wartość None.

from math import inf

def max_moves(x, y, forbidden, n, prev_move = None ):
    if (x,y) == (n-1,n-1):
        return 0
    if (x,y) in forbidden:
        return -inf
    if  not (0<=x<n and 0<=y<n):
        return -inf

    res = -inf

    if prev_move != "up": # czy moge w dol
        res = max(res, max_moves(x+1, y, forbidden, n, "down")+1)
    if prev_move != "down": # czy moge w gore
        res = max(res, max_moves(x-1, y, forbidden, n, "up")+1)
    res = (res, max_moves(x, y+1, forbidden, n, "right")+1)

    return res

def knight(n,l):
    result = max_moves(0,0,l, n)
    return None if result == -inf else result



