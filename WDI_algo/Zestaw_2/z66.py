# Napisać program wypełniający N-elementową tablicę T liczbami pseudolosowymi z zakresu
# 1-1000 i sprawdzający czy istnieje element tablicy zawierający wyłącznie cyfry nieparzyste.

import random
def check(x):
    while x>0:
        digit = x%10
        if digit%2==0:
            return False
        x//=10
    return True

def check_odd_digit(N):
    T = []  # Inicjalizacja pustej listy

    while len(T)<N:
        num = random.randint(1,1000)
        if check(num) is True:
            T.append(num)


    print(T)
    return T

check_odd_digit(10)