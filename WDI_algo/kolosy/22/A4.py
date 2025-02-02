# Na szachownicy o rozmiarach N × N reprezentowanej przez tablicę T[N][N] umieszczono pewną liczbę
# skoczków. Położenie skoczka w tablicy oznaczono liczbą 1, puste pola oznaczono liczbą 0. Część pustych pól
# na szachownicy jest szachowana przez znajdujące się na niej skoczki. Proszę zaproponować funkcję place(T),
# która znajdzie na szachownicy puste pole położone najbliżej środka szachownicy, takie że umieszczenie tam
# skoczka maksymalnie zwiększy liczbę szachowanych pustych pól.
# Do funkcji przekazujemy tablicę T zawierającą położenie skoczków.
# Funkcja powinna zwrócić pole (wiersz, kolumna), na którym należy umieścić
# skoczka. Odległość pomiędzy polami: (w1, k1) i (w2, k2) jest równa max(abs(w1 − w2), abs(k1 − k2))
from WDI_algo.Zestaw_3.z113 import distance


def place(t):
    n= len(t)
    center = (n//2, n//2)

    knight_moves = [ (-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

    def is_valid(x,y):
        return 0<=x<n and 0<=y<n

    def count_newly_attacked(x,y):
        """funkcja do liczenia szachowanych pol"""
        res = 0

        for dx, dy in knight_moves:
            nx, ny = x+dx, y+dy
            if is_valid(nx,ny) and t[nx][ny] == 0:
                res += 1

        if t[x][y] == 2: # 2 gdy pole jest juz szachowane
            res -= 1

        return res


    # zamieniamy wszystkie szachowane pola na 2
    for i in range(n):
        for j in range(n):
            if t[i][j] == 1:
                for dx, dy in knight_moves:
                    nx,ny = i+dx, j+dy
                    if is_valid(nx, ny) and t[nx][ny] == 0:
                        t[nx][ny] = 2

    best_position = None
    max_new_attacked = -1
    min_distance_to_center = n

    for i in range(n):
        for j in range(n):
            if t[i][j] != 1:
                new_attacked = count_newly_attacked(i,j)
                distance_to_center = max(abs(i-center[0]), abs(j-center[1]))

                if new_attacked > max_new_attacked or (new_attacked == max_new_attacked and distance_to_center<min_distance_to_center):
                    best_position = (i,j)
                    min_distance_to_center = distance_to_center
                    max_new_attacked = new_attacked

    return best_position






