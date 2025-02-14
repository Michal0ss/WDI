# Na szachownicy o wymiarach N × N umieszczono pewną liczbę pionków.
# Położenie pionków opisuje lista [(w0, k0),(w1, k1),(w2, k2), ...].
# W lewym górnym rogu szachownicy (o współrzędnych 0, 0) znajduje się
# król, który musi dotrzeć do prawego dolnego rogu szachownicy. Król może wykonywać ruchy w prawo, w
# dół lub w górę szachownicy, nie może zbijać pionków ani wracać na pole, na którym już był. Proszę napisać
# funkcję king(N,L), która zwróci maksymalną liczbę ruchów jakie może wykonać król na drodze do celu. Do
# funkcji należy przekazać wyłącznie dwa parametry: rozmiar szachownicy N oraz listę L zawierającą położenia pionków.
# Jeżeli dotarcie do celu nie jest możliwe funkcja powinna zwrócić wartość None.
from math import inf
def king(N,L):
    def legalne(x,y):
        return (0<=x<N) and (0<=y<N)

    def ruch(pos:tuple, prev_move=None): # pos = x,y

        if pos == (N-1,N-1):
            return 0
        if not legalne(pos[0], pos[1]):
            return inf
        if pos in L:
            return inf

        prawo = ruch((pos[0], pos[1]+1), "prawo")
        dol= ruch((pos[0]+1,pos[1]), "dol")

        if prev_move!="prawo":
            prawo+=1
        if prev_move!="dol":
            dol+=1
        return min(dol,prawo)
