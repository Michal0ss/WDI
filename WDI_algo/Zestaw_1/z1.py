# Proszę napisać program poszukujący trójkątów Pitagorejskich w których długość przekątnej (czyli przeciwprostokątnej c)
# jest mniejsza od liczby N wprowadzonej z klawiatury

from math import sqrt

def triangle(n):
    for a in range (1,n):
        #print(a,"a")
        for b in range(a,n):
            #print(b, "b")
            c_tr = a**2 + b**2
            c = int(sqrt(c_tr))
            if c**2 == c_tr and c<n:
                print(f"Znaleziono trójkąt Pitagorejski: a={a}, b={b}, c={c}")

N = int(input("Podaj liczbę N: "))

triangle(N)