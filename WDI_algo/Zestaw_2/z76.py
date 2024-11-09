# Dane są dwie N-elementowe tablice t1 i t2 zawierające liczby naturalne. Z wartości w
# obu tablicach możemy tworzyć sumy. „Poprawna” suma to taka, która zawiera co najmniej jeden element
# (z tablicy t1 lub t2) o każdym indeksie. Na przykład dla tablic: t1 = [1,3,2,4] i t2 = [9,7,4,8] poprawnymi
# sumami są na przykład 1+3+2+4, 9+7+4+8, 1+7+3+8, 1+9+7+2+4+8. Proszę napisać funkcje generującą
# i wypisująca wszystkie poprawne sumy, które są liczbami pierwszymi. Do funkcji należy przekazać dwie
# tablice, funkcja powinna zwrócić liczbę znalezionych i wypisanych sum.

import math


def czy_pierwsza(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def poprawne_sumy_pierwsze(t1, t2):
    n = len(t1)
    liczba_sum = 0

    for maska in range(1, 2 ** n):
        suma = 0
        poprawna_suma = False
        for i in range(n):
            if (maska // (2 ** i)) % 2 == 1:
                suma += t2[i]
                poprawna_suma = True
            else:
                suma += t1[i]

        print(f"Suma: {suma}, Czy liczba pierwsza: {czy_pierwsza(suma)}")

        if poprawna_suma and czy_pierwsza(suma):
            print(f"Poprawna suma będąca liczbą pierwszą: {suma}")
            liczba_sum += 1

    return liczba_sum


# Przykładowe tablice
t1 = [1,3,2,4]
t2 = [9,7,4,8]


# Wywołanie funkcji
liczba_sum = poprawne_sumy_pierwsze(t1, t2)
print(f"Liczba poprawnych sum będących liczbami pierwszymi: {liczba_sum}")
