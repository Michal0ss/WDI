# Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
# ta jest iloczynem dowolnych dwóch wyrazów ciągu Fibonacciego.
# 1 1 2 3 5 8 13 21 34 45


def multiply_fib(n):
    a,b=1,1
    m=0
    while a< 1_000_000:
        print(a)
        m=a*b
        temp=a+b
        a=b
        b=temp
        if n==m:
            return True

print(multiply_fib(15))

