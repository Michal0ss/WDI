#Dana jest N-elementowa tablica T, zawierająca liczby. Proszę napisać funkcję, która zwróci
#indeks największej liczby, która jest iloczynem wszystkich liczb pierwszych leżących w tablicy na indeksach
#mniejszych od niej, lub None jeżeli taka liczba nie istnieje.
from math import sqrt
def is_prime(n):
    if n<=1:
        return False
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def find(t):
    n= len(t)
    m=0
    for i in range(n):
        x=is_prime(t[i])
        m*=x
        for j in range(n):
            if m == t[j]:
                return True