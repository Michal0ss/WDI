def podz(n):
    """Funkcja generujaca podzielniki wlasciwe liczby n"""
    for p in range(1,n):
        if n%p ==0:
            yield p # print p

g = podz(24) # zmienna g od teraz to Generator

for i in podz(120):
    print(i, end=" ")
print()


l = [ x for x in g]
print(l)


n=24
z = (p for p in range(1,n) if n%p==0)
print(z)