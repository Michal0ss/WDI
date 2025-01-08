# ====================================================================================================>
# Zadanie 164
# Proszę napisać funkcję, która jako parametr otrzymuje liczbę naturalną i zwraca sumę
# iloczynów elementów wszystkich niepustych podzbiorów zbioru podzielników pierwszych tej liczby. Można
# założyć, że liczba podzielników pierwszych nie przekracza 20, zatem w pierwszym etapie funkcja powinna
# wpisać podzielniki do tablicyp pomocniczej. Przykład:60→[2,3,5]→2+3+5+2∗3+2∗5+3∗5+2∗3∗5=71
# ====================================================================================================>
# zadanie_164(60) -> print([2,3,5], 71)
from math import prod

def zad_164(num):
    def divisors(num):
        div = []
        i = 2
        while num > 1:
            if num % i == 0:
                div.append(i)
                while num % i == 0:
                    num //= i
            i += 1
        print(div, end="  ")
        return div


    def rek(primes, current_i=0, product=1):
        if current_i == len(primes):
            if product==1:
                return
            nonlocal s
            s += product
            #print(f"{product}+", end="")
            return
        rek(primes, current_i + 1, product)
        rek(primes, current_i + 1, product * primes[current_i])

    s=0

    rek(divisors(num))

    print(s)


x = int(input("podaj cyfre"))
zad_164(x)