# Proszę napisać program rozwiązujący równanie x^x = 2024 metodą bisekcji.

def f(x):
    #return (x**x)-2024
    return x**2 -4
def bisection(a, b , tolerance):
    #if f(a)*f(b) >= 0:
    #    print("Metoda bisekcji nie może być zastosowana na tym przedziale.")
    #    return None
#
    while abs((b-a)/2)>tolerance:
        c = (a+b)/2
        if f(c) == 0 :
            return c
        elif f(a)*f(c) < 0:
            b=c# Rozwiązanie jest w przedziale [a, c]
        else:
            a=c# Rozwiązanie jest w przedziale [c, b]
    return (a+b)/2

a, b = 1,3
print(bisection(a,b,1e-6))