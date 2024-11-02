# Proszę napisać program wczytujący dwie liczby naturalne a, b i wypisujący rozwinięcie dziesiętne ułamka a/b uwzględniając ułamki okresowe.
# Na przykład 2/3 = 0.(6), 1/5 = 0.2, 1/6 = 0.1(6), 1/7 = 0.(142857)

# Proszę napisać program wczytujący trzy liczby naturalne a, b, n i wypisujący rozwinięcie
# dziesiętne ułamka a/b z dokładnością do n miejsc po kropce dziesiętnej. (n jest rzędu 100)
import math
def  prime_factors(x):
    divider = 2
    while divider**2 <= x:
        while  x % divider == 0:
            x//=divider
    return x


def divide(a,b):
    for i in range(1,b+1):
        if a%i & b%i == 0:
            a//=i
            b//=i
    shorten_b = prime_factors(b)


a = int(input("Podaj licznik (a): "))
b = int(input("Podaj mianownik (b): "))

divide(a, b)