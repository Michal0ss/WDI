# Sudoku składa się kwadratu o wymiarach 9 × 9 podzielonego na 9 małych kwadratów o wymiarach 3 × 3.
# W poprawnym rozwiązaniu: w każdym wierszu, każdej kolumnie i każdym małym kwadracie znajdują się
# cyfry 1 − 9. W tablicy T[9][9] zawierającej poprawne rozwiązanie, ktoś je złośliwie uszkodził, zamieniając
# miejscami dwa małe kwadraty. Wiemy, że zamienione kwadraty leżały w różnych wierszach i różnych kolumnach.
# Zamiana spowodowała, że niektóre wiersze i niektóre kolumny zawierają powtarzające się cyfry.
# Proszę napisać funkcję repeair(T), która naprawi uszkodzoną tablicę. Do funkcji należy przekazać tablicę
# zawierającą uszkodzone rozwiązanie, funkcja powinna zwrócić informację czy zamiana dotyczyła środkowego
# małego kwadratu.


def is_valid(t):
    for i in range(9):
        preview_r, preview_c = [False for _ in range(9)], [False for _ in range(9)]
        for j in range(9):
            if preview_c[t[j][i]] or preview_r[t[i][j]]:
                return False
            preview_r[t[i][j]]=preview_c[t[j][i]]=True
    return True

def swap(t,a,b):
    """funkcja zamienia dwa kwadraty miejscami gdzie a i b to sa wspolrzedne lewego gornego wierzcholka
       """
    ax, ay = a[0], a[1]
    bx, by = b[0], b[1]
    offsets = [(0,0), (0,1), (0,2), (0,1), (1,1), (2,1), (0,2), (1,2), (2,2)]
    for x,y in offsets:
        t[ax+x][ay+y]= t[bx+x][by+y] # przenosimy z b do a
        t[bx + x][by + y] = t[ax+x][ay+y] # przenosimy z a do b

def repair(t):
    positions_of_squares =  [ (0, 0), (3, 0), (6, 0), (0, 3), (3, 3), (6, 3), (0, 6), (3, 6), (6, 6) ]

    for a in range(9):
        for b in range(a+1,9):
            swap(t, positions_of_squares[a], positions_of_squares[b])
            r = is_valid(t)
            swap(t, positions_of_squares[a], positions_of_squares[b])
            if r:
                return a==4,b==4 # (3,3)
    return None