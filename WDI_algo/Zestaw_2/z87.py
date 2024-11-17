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
    product = 1
    max_idx = None
    for i in range(n):
        # Check if the current number is prime
        if is_prime(t[i]):
            product *= t[i]

        # Check if the current number is equal to the product
        if t[i] == product:
            max_idx = i

    return max_idx

T = [2,2,3,2,99,24]
print(find(T))