# ====================================================================================================>
# Zadanie 150
# Dane są dwie liczby naturalne z których budujemy trzecią liczbę. W budowanej liczbie
# muszą wystąpić wszystkie cyfry występujące w liczbach wejściowych. Wzajemna kolejność cyfr każdej z liczb
# wejściowych musi być zachowana. Na przykład mając liczby 123 i 75 możemy zbudować liczby 12375,17523,
# 75123, 17253, itd. Proszę napisać funkcję która wyznaczy ile liczb pierwszych można zbudować z dwóch
# zadanych liczb.
# ====================================================================================================>

from math import log10, sqrt

def prime(n):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0 or n % 3 == 0:
        return False

    i = 5
    while i < sqrt(n) + 1:
        if n % i == 0:
            return False
        i += 2
        if n % i == 0:
            return False
        i += 4
    # end
    return True


def find_amount_nums(a,b):
    required_len = int(log10(a))+1 + int(log10(b))+1
    def recursion(a,b,c,i):
        if len(str(c)) == required_len:
            print(c)# Dodatkowy wydruk
                                                                    #if ((int(log10(c))+1) == required_len) and is_prime(c):
        if a == 0 and b == 0:
            return 0                                                #if is_prime(c):
                                                                    #    print(c)
                                                                    #    return 1

        if a==0:
            return recursion(a, 0, c+b*(10**i), i+1)
        if b==0:
            return recursion(0, b, c+a*(10**i), i+1 )
        return  recursion(a//10, b, c+ (a%10) *(10**i), i+1) + recursion(a, b//10, c+(b%10)*(10**i), i+1)

    return recursion(a,b,0,0)

a=75
b=123
print(find_amount_nums(123,75))

