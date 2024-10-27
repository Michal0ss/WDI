# Proszę napisać program sprawdzający czy zadana liczba jest pierwszą
from math import sqrt

def is_prime(n):

     if n<=1:
         return False

#Dlatego wystarczy sprawdzić dzielniki od 2 do sqrt(n) jeśli żaden z tych dzielników nie dzieli liczby n, oznacza to, że
# n nie ma innych dzielników poza 1 i samym sobą, czyli jest liczbą pierwszą.

     for i in range(2, int(sqrt(n))+1):
         if n%i==0:
             return False
     return True

n = int(input("Podaj liczbe"))

if is_prime(n):
    print("tak")
else:
    print("nie")
