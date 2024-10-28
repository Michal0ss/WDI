# Proszę napisać program wyznaczający wartość do której zmierza iloraz dwóch kolejnych
# wyrazów ciągu Fibonacciego. Wyznaczyć ten ilorazy dla różnych wartości dwóch początkowych wyrazów
# ciągu.
# 1 1 2 3 5 8 13 21 34 <-- traktujemy jako ciag geo
# obliczamy q wraz z kazdym kolejnym wyrazem dokladnosc q wzrasta
# obliczamy kolejne wartosci q petla while do momentu az q<=accuracy=1e-6
from sympy.polys.specialpolys import fateman_poly_F_1


#q=  1, 0.5, 2/3 ..... az dojdziemy do dokladnosci accuracy=1e-6


def limes_cipes(f0,f1, tolerance=1e-10):
    previous_q = 0
    a,b = f0, f1
    while True:

        temp = a+b
        a=b
        b=temp

        q = b/a

        if abs(q - previous_q) < tolerance:
            return q

        previous_q = q  # dla 3 5 -> previous_q= 5/3 dla 5 8 -> q =  8/5 ...

print(limes_cipes(1,1))
print(limes_cipes(2,3))
print(limes_cipes(3,5))
print(limes_cipes(13,21))