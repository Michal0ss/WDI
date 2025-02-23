# Dwie różne liczby nazywamy zaprzyjaźnionymi gdy każda jest równa sumie podzielników
# właściwych drugiej liczby, na przykład 220 i 284. Proszę napisać program wyszukujący liczby zaprzyjaźnione
# mniejsze od miliona.
from math import sqrt

#def friends_num(a,b):
#    sa=0
#    sb=0
#    n=0
#    #t_a=[]
#    #t_b=[]
#    for i in range(1, a):
#        if a%i==0:
#            print(i)
#            sa+=i
#    for j in range(1, b):
#        if b % j == 0:
#            print(j)
#            sb+=j
#    if sa == b and sb==a:
#       return True
#
#x = int(input(" podaj pierwsza"))
#y = int(input(" podaj pierwsza"))
#print(friends_num(x,y))


def suma_podzielnikow_wlasciwych(n):
    suma = 0
    # Sprawdzamy dzielniki do pierwiastka z n
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            suma += i
            if i != n // i and i != 1:  # Unikamy dodawania n i duplikacji
                suma += n // i
    return suma

def znajdz_zaprzyjaznione(maks):
    for a in range(2, maks):
        b = suma_podzielnikow_wlasciwych(a)
        if b > a and b < maks:  # Upewnij się, że b jest większe niż a i mniejsze niż maks
            if suma_podzielnikow_wlasciwych(b) == a:
                print(f"{a} i {b}")

# Wyszukiwanie liczb zaprzyjaźnionych mniejszych od miliona
maks = 1_000_000
print("Liczby zaprzyjaźnione mniejsze od miliona:")
znajdz_zaprzyjaznione(maks)

