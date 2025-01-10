# ====================================================================================================>
# Zadanie 168
# Dana jest liczba naturalna N. Proszę zaimplementować funkcję divide(N), która sprawdza
# czy jest możliwe pocięcie liczby N na kawałki, tak aby każdy z kawałków był liczba pierwszą oraz liczba kawał-
# ków też była liczbą pierwszą. Funkcja powinna zwracać wartość logiczną. Naprzykład: divide(2347)=True,
# podział na 23 i 47, natomiast divide(2255)=False.
# Przykładowe wywołania funkcji:
# print(divide(273)) # True, podział 2|7|3
# print(divide(22222)) # True, podział 2|2|2|2|2
# print(divide(23672)) # True, podział 23|67|2
# print(divide(2222)) # False
# print(divide(21722)) # False
# ====================================================================================================>

import math
def is_prime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False

    for i in range(6, int(num**0.5) + 3, 6):
        if num % (i + 1) == 0 or num % (i - 1) == 0:
            return False

    return True

def first_digit(n):
    length=int(math.log10(n))+1
    return n//10**(length-1)

def rek(num, nums, i , parts):

    if is_prime(num) and is_prime(parts):
        return True
    if i>num:
        return False
    if is_prime(num%i):
        if rek(num//i, [num%i]+nums, 10, parts+1):
            return True

    return rek(num, [*nums], i*10, parts)

def divide(num):

    return rek(num,[],10,1)







#def rek(num,digit, primes=[]):
#    if  is_prime(len(primes)) :
#        return True
#    if is_prime(digit):
#        return rek(num, digit, primes+[digit])
#    #if is_prime(first_digit(num)):
#    #    return rek(num%(int(math.log10(num))), idx+1, primes+[first_digit(num)])
#    else:
#        return rek(num, digit*)


