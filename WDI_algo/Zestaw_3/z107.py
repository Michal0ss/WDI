#Dana jest tablica T[N][N], wypełniona liczbami naturalnymi. Proszę napisać funkcję która
#odpowiada na pytanie, czy w tablicy każdy wiersz zawiera co najmniej jedną liczbą złożoną wyłącznie z cyfr
#będących liczbami pierwszymi?


import math
def does_num_contain_prime(x):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    while x>0:
        digit=x%10
        if is_prime(digit):
            return True
        x//=10
    return False

def find_that_num(t):
    N = len(t)
    for i in range(N):
        flag = False
        for j in range(N):
            if does_num_contain_prime(t[i][j]):
                flag = True
                break
        if not does_num_contain_prime(t[i][j]):
            return False
    return True



T = [
    [233, 18, 46],  # 233 składa się wyłącznie z cyfr będących liczbami pierwszymi (2, 3, 3)
    [12, 25, 66],   # 25 składa się wyłącznie z cyfr będących liczbami pierwszymi (2, 5)
    [3, 7, 3]      # Brak liczby złożonej wyłącznie z cyfr będących liczbami pierwszymi
]

print(find_that_num(T))