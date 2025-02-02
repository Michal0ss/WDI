# ====================================================================================================>
# Zadanie A5, 17.01.2023
# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi, na której możemy wykonywać operacje:
# • rotacji elementów danego wiersza w prawo,
# • rotacji elementów danej kolumny w dół.
# Tablicę taką nazywamy kwadratem magicznym, wtedy gdy suma elementów w każdym wierszu i każdej kolumnie jest jednakowa.
# Proszę napisać funkcję magic(T), która sprawdza czy po wykonaniu dokładnie dwóch
# dowolnych operacji tablica T stanie się kwadratem magicznym. Funkcja powinna zwrócić True albo F alse.
# Na przykład dla tablicy:
# 3 11 14 17
# 6 12 7 9
# 10 8 16 13
# 5 15 4 2
# po wykonaniu rotacji wiersza 0, następnie rotacji kolumny 2, tablica będzie kwadratem magicznym.
# ====================================================================================================>


def rotate_to_right(t, idx):
    n = len(t)
    last = t[idx][-1] #ostatni element wiersza
    for i in range(n-1,0 ,-1):
        t[idx][i] = t[idx][i-1]
    t[idx][0] = last


def rotate_down(t, idx):
    n = len(t)
    last = t[-1][idx]  # ostatni element wiersza
    for i in range(n - 1, 0, -1):
        t[i][idx] = t[i-1][idx]
    t[0][idx] = last



def sum_every_w_c(t):
    n=len(t)
    target_sum_r = sum(t[0][j] for j in range(n))
    target_sum_c = sum(t[i][0] for i in range(n))

    for i in range(n):
        sum_r = 0
        sum_c = 0
        for j in range(n):
            sum_r += t[i][j]
            sum_c += t[j][i]
        if sum_r != target_sum_r or sum_c != target_sum_c:
            return False

    return True



def magic(t):
    n = len(t)
    operations = [
        (rotate_down, rotate_down),
        (rotate_to_right, rotate_to_right),
        (rotate_to_right, rotate_down),
        (rotate_down, rotate_to_right)
    ]

    for i in range(n):
        for j in range(n):
            for op1, op2 in operations:
                ...