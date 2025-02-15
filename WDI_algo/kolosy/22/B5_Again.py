# Sudoku składa się kwadratu o wymiarach 9 × 9 podzielonego na 9 małych kwadratów o wymiarach 3 × 3.
# W poprawnym rozwiązaniu: w każdym wierszu, każdej kolumnie i każdym małym kwadracie znajdują się
# cyfry 1 − 9. W tablicy T[9][9] zawierającej poprawne rozwiązanie, ktoś je złośliwie uszkodził, zamieniając
# miejscami dwa małe kwadraty. Wiemy, że zamienione kwadraty leżały w różnych wierszach i różnych kolumnach.
# Zamiana spowodowała, że niektóre wiersze i niektóre kolumny zawierają powtarzające się cyfry.
# Proszę napisać funkcję repeair(T), która naprawi uszkodzoną tablicę. Do funkcji należy przekazać tablicę
# zawierającą uszkodzone rozwiązanie, funkcja powinna zwrócić informację czy zamiana dotyczyła środkowego
# małego kwadratu.

def isvalid(a):
    for i in range(9):
        appear_r, appear_c = [False for _ in range(10)], [False for _ in range(10)]

        for j in range(9):
            if appear_r[a[i][j]] or appear_c[a[j][i]]:
                return False

            appear_r[a[i][j]]=appear_c[a[j][i]]=True

    return True

def swap(t,a,b):
    ax, ay = a[0], a[1] # a to wsporzedne x krawedzi kwadratu (lewej)
    bx, by = b[0], b[1]
    subgrid_offset = [(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)]
    for x,y in subgrid_offset:
        t[ax+x][ay+y], t[bx+x][by+y] = t[bx+x][by+y], t[ax+x][ay+y]


def repair(t):
    subgrid_top_left = [(0,0), (0,3), (0,6), (3, 0), (3,3), (3,6), (6,0), (6,3), (6,6)]
    for i in range(9):
        for j in range(i+1, 9):
            swap(t,subgrid_top_left[i], subgrid_top_left[j])
            r = isvalid(t)
            swap(t, subgrid_top_left[i], subgrid_top_left[j])
            if r:
                return i == 4 and j == 4
    return None