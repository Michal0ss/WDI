#Liczba Smitha to taka, której suma cyfr jest równa sumie cyfr wszystkich liczb występujących
#w jej rozkładzie na czynniki pierwsze. Na przykład: 85 = 5 ∗ 17, 8 + 5 = 5 + 1 + 7. Proszę napisać program
#wypisujący liczby Smitha mniejsze od 10^6.

import math

#def divide(n):
#    sum_divider=0
#    for i in range(1,int(math.sqrt(n))+1):
#        original_i = i
#        if n%i==0:
#            n//=i
#            while original_i>0:
#                digit=original_i%10
#                sum_divider+=digit
#                original_i//=10
#    return sum_divider


#def smith():
#    sum=0
#    for n in range(2, 10**6+1):
#        while n > 0:
#            digit = n%10
#            sum+=digit
#            n//=10

#            if divide(n)==sum:
#                print(n)


import math


def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


def prime_factorization(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i

    if n > 2:
        factors.append(n)

    return factors


def is_smith_number(n):
    if n < 2:
        return False

    factors = prime_factorization(n)

    if len(factors) == 1:
        return False  # Liczby pierwsze nie są liczbami Smitha

    sum_digits_n = sum_of_digits(n)
    sum_digits_factors = sum(sum_of_digits(factor) for factor in factors)

    return sum_digits_n == sum_digits_factors


def smith():
    for n in range(2, 10 ** 6):
        if is_smith_number(n):
            print(n)


smith()
