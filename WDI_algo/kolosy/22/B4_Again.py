# Na szachownicy o rozmiarach N × N reprezentowanej przez tablicę T[N][N] umieszczono pewną liczbę
# wież szachowych tak, że każde z wolnych pól na szachownicy jest szachowane. Położenie wież w tablicy
# oznaczono wartościami True. Przyszedł zły człowiek i zmienił położenie jednej z wież na szachownicy, tak że
# nie wszystkie wolne pola są szachowane. Proszę zaproponować funkcję move(T), która znajdzie przeniesienie
# jednej wieży, tak aby ponownie wszystkie pola były szachowane.
# Do funkcji przekazujemy tablicę T zawierającą położenie wież po zmianie położenia wieży.
# Funkcja powinna zwrócić dwa pola (wiersz, kolumna) – skąd i dokąd należy przenieść wieżę.
from WDI_algo.Zestaw_3.z116_HARD import szachownica


def atakowane_pola(t):
    n=len(t)
    szachowane=[[False for _ in range(n)]for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if t[i][j]:
                for k in range(n):
                    szachowane[i][k] = True
                    szachowane[k][i] = True

    for i in range(n):
        for j in range(n):
            if not szachowane[i][j]:
                return False
    return True

def move(t):
    n=len(t)
    for i in range(n):
        for j in range(n):
            if t[i][j]:
                t[i][j] = False # podmieniam
                for k in range(n):
                    for z in range(n):
                        if not t[k][z]:
                            t[k][z]=True
                            if atakowane_pola(t):
                                return (i,j), (k,z)
                            t[k][z]=False
                t[i][j]=True # wracam do tego co bylo
    return