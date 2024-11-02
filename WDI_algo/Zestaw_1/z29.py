# Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
# ta jest wielokrotnością dowolnego wyrazu ciągu danego wzorem An = n ∗ n + n + 1.

# np. A2 = 2*2+2+1= 7 => sprawdz czy dla n%7==0

import math

def is_multiply_of_sequence(n):
    k=1
    while True:
        an = k*k + k + 1
        if an>n:
            break
        if n%an ==0:
            return True
        k+=1
    return False


n = int(input("Podaj liczbe naturalna: "))

if n > 0:
    if is_multiply_of_sequence(n):
        print(f"Liczba {n} jest wielokrotnością przynajmniej jednego wyrazu ciągu An = n^2 + n + 1.")
    else:
        print(f"Liczba {n} nie jest wielokrotnością żadnego wyrazu ciągu An = n^2 + n + 1.")
else:
    raise ValueError("Liczba musi być naturalna (większa od zera).")