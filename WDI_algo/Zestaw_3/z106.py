#Dana jest tablica T[N][N], wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
#odpowiada na pytanie, czy w tablicy istnieje wiersz, w którym każda liczba zawiera co najmniej jedną cyfrę
#będącą liczbą pierwszą?

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
        flag = True
        for j in range(N):
            if not does_num_contain_prime(t[i][j]):
                flag =False
                break
        if does_num_contain_prime(t[i][j]):
            return True
    return False

T = [
    [46, 18, 46],
    [12, 26, 66],
    [8, 9, 14]
]

print(find_that_num(T))  # True, bo pierwszy wiersz spełnia warunek (każda liczba zawiera cyfrę pierwszą).
