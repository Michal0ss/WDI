# Na szachownicy o rozmiarach N × N reprezentowanej przez tablicę T[N][N] umieszczono pewną liczbę
# wież szachowych tak, że każde z wolnych pól na szachownicy jest szachowane. Położenie wież w tablicy
    # oznaczono wartościami True. Przyszedł zły człowiek i zmienił położenie jednej z wież na szachownicy, tak że
# nie wszystkie wolne pola są szachowane. Proszę zaproponować funkcję move(T), która znajdzie przeniesienie
# jednej wieży, tak aby ponownie wszystkie pola były szachowane.
# Do funkcji przekazujemy tablicę T zawierającą położenie wież po zmianie położenia wieży.
# Funkcja powinna zwrócić dwa pola (wiersz, kolumna) – skąd i dokąd należy przenieść wieżę.

def wszystkie_szachowane(t):
    """sprawdz czy wszystkie pola szachownicy t sa szachowane"""
    n=len(t)
    szachowane = [[False for _ in range(n)] for _ in range(n)]

    # zapisuje ktore pola sa szachowane wraz z polami na kotrych sa wierze
    for i in range(n):
        for j in range(n):
            if t[i][j]:
                for k in range(n):
                    szachowane[i][k] = True
                    szachowane[k][j] = True

    #sprawdz czy wszystkie pola szachownicy sa szachowane
    for i in range(n):
        for j in range(n):
            if not t[i][j]:
                return False
    return True

def move(t):
    n = len(t)
    for i in range(n):
        for j in range(n):
            if t[i][j]:
                t[i][j]=False

                for k in range(n):
                    for l in range(n):
                        if not t[k][l]:
                            t[k][l]=True
                            if wszystkie_szachowane(t):
                                return (i,j), (k,l)
                            t[k][l]=False
                t[i][j]=True

    return
