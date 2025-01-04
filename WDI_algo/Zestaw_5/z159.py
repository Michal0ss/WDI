# ====================================================================================================>
# Zadanie 159
# Do budowy liczby naturalnej reprezentowanej w systemie dwójkowym możemy użyć A
# cyfr 1 oraz B cyfr 0, gdzie A,B > 0. Proszę napisać funkcję, która dla zadanych parametrów A i B zwraca
# ilość wszystkich możliwych do zbudowania liczb,takich że pierwsza cyfra w systemie dwójkowym (najstarszy
# bit) jest równa 1, a zbudowana liczba jest złożona. Na przykład dla A=2, B=3 ilość liczb wynosi 3, są to
# 10010 ,10100 ,11000
# (2) (2) (2)
# ====================================================================================================>
from math import sqrt

def is_prime(x):
    if x == 2 or x ==3:
        return True
    if x <=1 or x % 2 == 0 or x%3 ==0:
        return False

    i = 5
    while i <= sqrt(x) +1:
        if x%i == 0:
            return False
        i+=2
        if x%i == 0:
            return False
        i+=4

    return True

def rek_10_to_2(n):
    if n == 0:
        return 0
    if n ==1:
        return 1
    return rek_10_to_2(n//2)*10 + n%2

def zad_159(A,B):
    num = 2**(A+B-1) # tworzymy liczbe z pierwszym bitem czyli 1 na poczatku
    suma = 0

    def rek(A,B,num):
        nonlocal suma
        if A == 0 and B == 0:
            if not is_prime(num):
                suma +=1
                print(num, rek_10_to_2(num))
            return
        if A > 0:
            rek(A-1, B, num + 2 ** (A + B -1))
        if B > 0:
            rek(A,B-1, num)

    rek(A-1, B, num)
    return suma





print(zad_159(2, 3))
