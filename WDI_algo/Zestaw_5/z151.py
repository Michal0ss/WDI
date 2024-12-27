# ====================================================================================================>
# Zadanie 151
# W szachownicy o wymiarach 8x8 każdemu z pól przypisano liczbę naturalną. Na ruchy
# króla nałożono dwa ograniczenia: król może przesunąć się na jedno z 8 sąsiednich pól jeżeli ostatnia cyfra
# liczby na polu na którym stoi jest mniejsza od pierwszej cyfry liczby pola docelowego, oraz w drodze do
# obranego celu(np.narożnika) król nie może wykonaćl ruchu, który powoduje oddale niego od celu. Dana jest
# globalna tablica T[8][8] wypełniona liczbami naturalnymi reprezentująca szachownicę. Lewy górny narożnik
# ma współrzędne w=0 i k=0. Proszę napisać funkcję sprawdzającą czy król może dostać się z pola w,k do
# prawego dolnego narożnika.
# ====================================================================================================>
# return bool

import math

#jeżeli ostatnia cyfra liczby na polu na którym stoi jest mniejsza od pierwszej cyfry liczby pola docelowego,
# oraz w drodze do obranego celu(np.narożnika) król nie może wykonaćl ruchu, który powoduje oddale niego od celu

# Funkcja do wyciągania pierwszej cyfry liczby
def condition_first(x):
    length = int(math.log10(x)) + 1
    return x // 10 ** (length - 1)


# Funkcja sprawdzająca możliwy ruch króla
def move(t, w, k, n):
    if w + 1 < n and condition_first(t[w + 1][k]) > t[w][k] % 10:  # dół
        return 1
    elif w + 1 < n and k + 1 < n and condition_first(t[w + 1][k + 1]) > t[w][k] % 10:  # ukos w dół-prawo
        return 2
    elif k + 1 < n and condition_first(t[w][k + 1]) > t[w][k] % 10:  # prawo
        return 3
    return 0  # brak możliwego ruchu


# Rekurencyjna funkcja sprawdzająca, czy król może dojść do celu
def rek(t, w=0, k=0):
    n = len(t)
    if w == n - 1 and k == n - 1:  # Jeśli osiągnięto prawy dolny narożnik
        return True
    m = move(t, w, k, n)  # Sprawdź możliwy ruch
    if m == 1:  # Ruch w dół
        return rek(t, w + 1, k)
    elif m == 2:  # Ruch ukos w dół-prawo
        return rek(t, w + 1, k + 1)
    elif m == 3:  # Ruch w prawo
        return rek(t, w, k + 1)
    return False  # Jeśli żaden ruch nie jest możliwy


T = [
                    [3, 5, 7, 2, 4, 1, 6, 8],
                    [6, 4, 8, 1, 7, 2, 5, 3],
                    [5, 7, 6, 3, 1, 4, 8, 2],
                    [1, 2, 3, 5, 8, 6, 4, 7],
                    [7, 8, 5, 4, 6, 3, 1, 2],
                    [2, 6, 3, 7, 5, 4, 8, 1],
                    [8, 1, 2, 4, 3, 7, 6, 5],
                    [4, 3, 6, 8, 2, 5, 7, 1],
                ]
print(rek(T))  # Sprawdź, czy król może dotrzeć do prawego dolnego narożnika

