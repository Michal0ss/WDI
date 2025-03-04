#   Dany jest ciąg zer i jedynek zapisany w tablicy T[N].
#   Proszę napisać funkcję, która odpowiada na pytanie czy jest możliwe pocięcie ciągu na kawałki
#   z których każdy reprezentuje liczbę pierwszą. Długość każdego z kawałków nie może przekraczać 30.
#   Na przykład dla ciągu 111011 jest to możliwe, a dla ciągu 110100 nie jest możliwe.

from math import sqrt



def prime(n):
    """Sprawdza, czy liczba n jest pierwsza."""
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
        if n % i == 0:
            return False
        i += 4
    return True


def Zadanie_137(T):
    def rek(T, i, x, k):
        x *= 2
        x += T[i]

        if i - k + 1 > 30:
            return False

        if i == len(T) - 1:
            if prime(x):
                return True
            return False

        if prime(x):
            return rek(T, i + 1, 0, i + 1) or rek(T, i + 1, x, k)
        return rek(T, i + 1, x, k)

    return rek(T, 0, 0, 0)


# Testy
print(Zadanie_137([1, 1, 1, 0, 1, 1]))  # True (111011)
print(Zadanie_137([1, 1, 0, 1, 0, 0]))  # False (110100)
