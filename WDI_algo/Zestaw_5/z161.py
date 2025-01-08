# ====================================================================================================>
# Zadanie 161
# Dany jest zbiór N liczb naturalnych umieszczony w tablicy T[N]. Proszę napisać funkcję,
# która zwraca informację, czy jest możliwy podział zbioru N liczb na trzy podzbiory, tak aby w każdym
# podzbiorze, łączna liczba jedynek użyta do zapisu elementów tego podzbioru w systemie dwójkowym była
# jednakowa. Na przykład: [2,3,5,7,15] → true, bo podzbiory {2,7} {3,5} {15} wymagają użycia 4 jedynek,
# [5,7,15]→false, podział nie istnieje.
# ====================================================================================================>
def count_ones(num):
    counter = 0
    while counter > 0:
        counter += num %2 # zliczy mi odrazu jedynki bo jak bedzie zero to suma licznika sie nie zmieni
        num //= 2
    return counter

def zad_161(t):

    arr_of_ones = [count_ones(x) for x in t] # tablica ilosci jedynek w zapisie (2) kazdej liczby z listy

    sum_ones = sum(arr_of_ones)

    if sum_ones % 3 != 0:
        return False
        # zeby podzbioty wedlug warunkow istnialy suma wszystkich jedynek musi byc podzielna przez 3 ze wzgledu
        # na ilosc podzbiorow

    wanted = sum_ones // 3

    def rek(A,B,C, idx):

        if idx == len(t):
            return True

        n = arr_of_ones[idx]

        if A+n <= wanted and rek(A+n, B, C, idx +1):
            return True
        if B+n <= wanted and rek(A, B+n, C, idx +1):
            return True
        if C+n <= wanted and rek(A, B, C+n, idx +1):
            return True

        return False
    return rek(0,0,0,0)



