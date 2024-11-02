# Napisać program generujący i wypisujący liczby pierwsze mniejsze od N metodą Sita Eratostenesa
from math import sqrt
def sito(n):
    primes = [True for _ in range(n)]
    primes[0]= False
    primes[1]=True

    for i in range(2,sqrt(n)+1):
        if primes[i]== True:
            for j in range(i**2, n, i):
                primes[j]=False

    for i in range(2, n):
        if primes[i]==True:
            print(i)