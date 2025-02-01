# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę zaimplementować funkcję
# trojki(T), która zlicza wszystkie trójki liczb, które spełniają następujące warunki:
# (1 ) Największym wspólnym dzielnikiem trzech liczb jest liczba 1,
# (2 ) W każdej trójce dwie dowolne liczby leżą w róznych wierszach i różnych kolumnach.
# Funkcja powinna zwrócić liczbę znalezionych trójek.

def check_nwd(a,b):
    while b:
        a, b=b, a%b
    return a
def gcd3(a,b,c):
    return check_nwd(check_nwd(a,b),c)

def trojki(t):
    count=0
    n = len(t)
    for r1 in range(n):
        for r2 in range(n):
            if r2==r1:
                continue
            for r3 in range(n):
                if r3 == r2 or r3 ==r1:
                    continue


                for c1 in range(n):
                    for c2 in range(n):
                        if c2 ==c1:
                            continue
                        for c3 in range(n):
                            if c3==c1 or c3==c2:
                                continue

                            a,b,c = t[r1,c1], t[r2,c2], t[r3][c3]

                            if gcd3(a,b,c) == 1:
                                count+=1
    return count