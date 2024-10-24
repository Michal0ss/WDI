# Napisać funkcję zamieniającą i wypisującą liczbę naturalną na system o podstawie 2-16.

def bin(n):
    tab=[0 for i in range(64)]
    i=0
    while (n>0):
        tab[i]=n%2
        n//=2
        i+=1
    i-=1
    while (i>=0):
        print(tab[i], end="")
        i-=1
    print()

print(bin(23))