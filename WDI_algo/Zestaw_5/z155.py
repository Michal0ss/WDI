# ====================================================================================================>
# Zadanie 155
# Dana jest tablica T[N] zawierająca liczby naturalne. Po tablicy możemy przemieszczać się
# według następującej zasady: z pola o indeksie i możemy przeskoczyć na pole o indeksie i+k jeżeli k jest
# czynnikiem pierwszym liczby t[i] mniejszym od t[i]. Proszę napisać funkcję, która zwraca informację czy jest
# możliwe przejście z pola o indeksie 0 na pole o indeksie N-1. Funkcja powinna zwrócić liczbę wykonanych
# skoków lub wartość -1 jeżeli powyższe przejście nie jest możliwe.
# ====================================================================================================>
from math import sqrt



def prime_factors(x):
    primes=[]
    for i in range(2, int(sqrt(x))+1):
        while x%i==0:
            primes.append(i)
            x//=i
    if x>1:
        primes.append(x)
    return primes


def zad_155(t):
    def rek(i, amount): # i to aktualny idx, k to wartosc z warunkow do przeskoczenie idx
        if i==len(t)-1:
            return amount
        if i>=len(t):
            return -1

        for k in prime_factors(t[i]):
            if k<t[i]:
                result = rek(i + k, amount + 1)
                if result != -1:
                    return result

        return -1

    return rek(0,0)


t=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
result = zad_155(t)
print(f"Liczba skoków: {result}")
