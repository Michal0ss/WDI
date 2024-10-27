# Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
# ta jest iloczynem dowolnych dwóch kolejnych wyrazów ciągu Fibonacciego.

def fib(n):
    a=1
    b=1

    while a * b < n :
        temp = b
        b=a+b
        a=temp
        #c=a+b
        #a = b
        #b=c
    return a*b==n


n = int(input("podaj naturalna"))
if fib(n):
    print("Tak, podana liczba jest iloczynem dwóch kolejnych wyrazów ciągu Fibonacciego.")
else:
    print("Nie, podana liczba nie jest iloczynem dwóch kolejnych wyrazów ciągu Fibonacciego.")