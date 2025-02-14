# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi, na której możemy wykonywać operacje:
# • rotacji elementów danego wiersza w prawo,
# • rotacji elementów danej kolumny w dół.
# Tablicę taką nazywamy kwadratem magicznym, wtedy gdy suma elementów w każdym wierszu i każdej kolumnie jest jednakowa.
# Proszę napisać funkcję magic(T), która sprawdza czy po wykonaniu dokładnie dwóch
# dowolnych operacji tablica T stanie się kwadratem magicznym. Funkcja powinna zwrócić T rue albo F alse.
# Na przykład dla tablicy:
# 3 11 14 17
# 6 12 7 9
# 10 8 16 13
# 5 15 4 2
# po wykonaniu rotacji wiersza 0, następnie rotacji kolumny 2, tablica będzie kwadratem magicznym.

def rotate_right(t,idx):
    ...
def rotate_down(t,idx):
    ...

def check_sum(t):
    n=len(t)
    target_sumw= sum(t[0][i] for i in range(n))
    target_sumk=sum(t[i][0] for i in range(n))

    for i in range(1,n):
        sumw=0
        sumk=0
        for j in range(1,n):
            sumw+=t[i][j]
            sumk+=t[j][i]
        if sumw != target_sumw and sumk != target_sumk:
            return False
    return True

def magic(t):
    n=len(t)
    possible_rotations = [
        (rotate_right, rotate_down),
        (rotate_down,rotate_right),
        (rotate_down, rotate_down),
        (rotate_right , rotate_right)
    ]

    for i in range(n):
        for j in range(n):
            for op1, op2 in possible_rotations:
                op1(t,i)
                op2(t,j)

                if check_sum(t):
                    return True

                if op1 == rotate_right:
                    rotate_right(t,i)
                else:
                    rotate_down(t,i)

                if op2 == rotate_right:
                    rotate_right(t,j)
                else:
                    rotate_down(t,j)

    return False