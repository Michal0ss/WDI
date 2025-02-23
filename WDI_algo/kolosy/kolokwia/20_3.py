# ====================================================================================================>
# Zadanie 3 2020
# Dana jest tablica T[N][N] (reprezentująca szachownicę) wypełniona liczbami całkowitymi.
# Proszę zaimplementować funkcję chess(T) która ustawia na szachownicy dwie wieże, tak aby suma liczb na
# „szachowanych” przez wieże polach była największa. Do funkcji należy przekazać tablicę, funkcja powinna
# zwrócić położenie wież w postaci krotki (row ,col ,row ,col ).
# Uwaga: zakładamy, że pola na których znajdują się wieże nie są szachowane.
# Przykładowe wywołania funkcji:
# print(chess([
# [4,0,2],
# [3,0,0],
# [6,5,3]])) # (0,1,1,0) suma=17
# print(chess([[1,1,2,3],[-1,3,-1,4], [4,1,5,4], [5,0,3,6]] # (2,3,3,1) suma=35
# ====================================================================================================>

def attack(t, rook1, rook2):
    n=len(t)
    # rook1 i rook2 to krotki gdzie rook1[0] to wiersz a rook1[1] to kolumna
    nx,ny=rook1
    mx,my=rook2
    sum1, sum2 =0,0
    attacked_positions = set()

    for i in range(n):
        if (i, ny) != rook1:
            sum1 += t[i][ny]
            attacked_positions.add((i,ny))
        if (nx, i) != rook1:
            sum1 += t[nx][i]
            attacked_positions.add((nx, i))

    for i in range(n):
        if (i,my)!=rook2 and (i,my) not in attacked_positions:
            sum2 += t[i][my]
        if (mx, i)!= rook2 and (mx,i) not in attacked_positions:
            sum2+=t[mx][i]
    return sum1, sum2

def find(t):
    n=len(t)
    best_pos = 0
    best_sum=-1
    for i in range(n):
        for j in range(n):
            for k in range(n):
                for m in range(n):
                    if (i, j) == (k, m):
                        continue  # Wieże nie mogą stać na tym samym polu

                    sum1, sum2 = attack(t, (i, j), (k, m))
                    total_sum = sum1 + sum2
                    if total_sum > best_sum:
                        best_sum = total_sum
                        best_pos = (i, j, k, m)

    return best_pos
