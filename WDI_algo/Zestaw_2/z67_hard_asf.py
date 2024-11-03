# Dana jest N-elementowa tablica T zawierająca liczby naturalne.
# W tablicy możemy przeskoczyć z pola o indeksie "k" o "n" pól w prawo jeżeli wartość n jest czynnikiem pierwszym liczby T[k].
# Napisać funkcję sprawdzającą czy jest możliwe przejście z pierwszego pola tablicy na ostatnie pole.
from math import sqrt
def is_prime(n):
    if n<=1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def prime_factors(n):
    factors = []
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            factors.append(i)
    return factors

def can_reach_end(T):
    n=len(T)
    visited = [False for _ in range(n)]
    stack=[0]

    while stack:
        current = stack.pop(0)
        if current == n-1:
            return True
        if not visited[current]:
            visited[current] = True
            factors = prime_factors(T[current])
            for factor in factors:
                next_index = current + factor
                if next_index < n:
                    stack.append(next_index)

        return False

T = [6, 10, 15, 3, 5]
print(can_reach_end(T))  # Zwraca True lub False w zależności od możliwości przejścia