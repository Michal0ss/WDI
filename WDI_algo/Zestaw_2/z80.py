# Dana jest tablica T[N] wypełniona niepowtarzającymi się liczbami naturalnymi.
# Proszę napisać funkcję trojki(T) która zlicza wszystkie trójki liczb, które spełniają następujące warunki:
# (1) największym wspólnym dzielnikiem trzech liczb jest liczba 1,
# (2) pomiędzy dwoma kolejnymi elementami trójki może być co najwyżej jedna przerwa.
# Funkcja powinna zwrócić liczbę znalezionych trójek

def nwd(a,b):

    while b!=0:
        temp = b
        b=a%b
        a=temp
    return a

def tri_nwd(a,b,c):
    return nwd(nwd(a,b), c)

def trios(t):
    triplets = []
    n=len(t)
    count=0
    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if tri_nwd(t[i], t[j], t[k]) == 1:
                    count+=1
                    triplets += [(t[i], t[j], t[k])]
    print(count)
    return triplets

numbers = [1, 2, 3, 4, 5]
triplets = trios(numbers)
print(triplets)
