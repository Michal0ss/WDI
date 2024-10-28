# Nieskończony iloczyn ... ma wartość 2/π. Proszę napisać program korzystający z tej zależności i wyznaczający wartość π.
from math import sqrt

def pi(accuracy=1e-6):
    num=sqrt(0.5)# Inicjalizujemy iloczyn pierwszym wyrazem
    product= num # iloczyn = wyraz
    before = 0
    now = 2 / product# Pierwsze przybliżenie π

    while abs(now-before)>accuracy:
        before=now
        num = sqrt(0.5 + 0.5 * num) # Obliczamy kolejny wyraz
        product *= num# Akumulujemy iloczyn
        now = 2/product# Obliczamy nowe przybliżenie π
    return now

pi = pi(accuracy=1e-6)
print(pi)