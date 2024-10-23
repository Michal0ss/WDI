from math import sqrt

def delta(a, b, c):
    e = b**2 - 4*a*c
    return e

def m_zer(a, b, c):
    d = delta(a, b, c)
    if d >= 0:
        return ((-b - sqrt(d)) / (2*a), (-b + sqrt(d)) / (2*a))
    return None


a = float(input("Podaj a: "))
b = float(input("Podaj b: "))
c = float(input("Podaj c: "))


if delta(a, b, c) > 0:
    print("Równanie ma dwa miejsca zerowe:", m_zer(a, b, c))
elif delta(a, b, c) == 0:
    print("Równanie ma jedno miejsce zerowe:", m_zer(a, b, c)[0])
else:
    print("Równanie nie ma miejsc zerowych.")


d = delta(a,b,c)
print(d)