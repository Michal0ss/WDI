# Proszę znaleźć najmniejszą liczbę pierwszą, której suma cyfr wynosi 101, a cyfry są w
# porządku nierosnącym

import math

def sum_digits(x):
    s=0
    before_digit=0
    while x>0:
        digit = x%10
        if digit <= before_digit:
            return False
        s+=digit
        before_digit=digit
        x//=10
    return s

def is_prime(x):
    for i in range(2, int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True

def find_num(s):
    x=2
    while True:
        if sum_digits(x)==s and is_prime(x):
            return x, True
        x+=1
        #if s==sum_digits(x):
        #    if is_prime(x):
        #        print(x)
        #        return True

print(find_num(11))