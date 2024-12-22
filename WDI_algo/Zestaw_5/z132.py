# ====================================================================================================>
# Zadanie 132
# Korzystając z zależności: symbol newtona(n|k) = symbol newtona(n-1|k-1) + symbol newtona(n-1|k)
# proszę napisać funkcję obliczającą wartość symbolu Newtona dla argumentów n i k.
# ====================================================================================================>


def symbol_newton(n, k):
    if k==0 or k==n:
        return 1
    return symbol_newton(n-1,k-1) + symbol_newton(n-1,k)

def zadanie_132(n,k):
    if k*2>n:
        return symbol_newton(n,n-k)
    return symbol_newton(n,k)