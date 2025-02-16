# ====================================================================================================>
# Zadanie A4, 20.12.2022
# Na szachownicy o rozmiarach N × N reprezentowanej przez tablicę T[N][N] umieszczono pewną liczbę
# skoczków. Położenie skoczka w tablicy oznaczono liczbą 1, puste pola oznaczono liczbą 0. Część pustych pól
# na szachownicy jest szachowana przez znajdujące się na niej skoczki. Proszę zaproponować funkcję place(T),
# która znajdzie na szachownicy puste pole położone najbliżej środka szachownicy, takie że umieszczenie tam
# skoczka maksymalnie zwiększy liczbę szachowanych pustych pól. Do funkcji przekazujemy tablicę T zawierającą położenie skoczków.
# Funkcja powinna zwrócić pole (wiersz, kolumna), na którym należy umieścić
# skoczka. Odległość pomiędzy polami: (w1, k1) i (w2, k2) jest równa max(abs(w1 − w2), abs(k1 − k2))
# ====================================================================================================>

def attack(t)->list[list[int]]:
    """funkcja ktora tworzy tablice boolean gdzie true to atakowane pola przez skoczka opisanego polem o wartosci 1"""
    n=len(t)
    knight = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
    for i in range(n):
        for j in range(n):
            if t[i][j]==1:
                for dx, dy in knight:
                    nx, ny = i+dx, j+dy
                    if 0<=nx<n and 0<=ny<n and t[nx][ny]<1:
                        t[nx][ny] = 2
    return t

def place(t):
    """funkcja ktora znajduje jak nablizszej srodka=center miejsca dla skoczka aby atakowal jak najwiecej pol"""
    n=len(t)
    max_amount_att=-1
    counter = 0
    center = (n//2, n//2)
    knight = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
    list_attacked = attack(t)
    for i in range(n):
        for j in range(n):
            if t[i][j] == 0:
                for dx, dy in knight:
                    nx, ny = i+dx, j+dy
                    if 0<=nx<n and 0<=ny<n and list_attacked[nx][ny]<1:
                        counter+=1
                    max_amount_att=max(max_amount_att, counter)





