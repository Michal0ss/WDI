# Proszę napisać program wypisujący podzielniki liczby

def divide(n):

    for i in range(1, n+1):
        if n%i==0:
            print (i)

n = int(input("podaj naturalna "))

divide(n)
