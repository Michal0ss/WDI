# Dwie liczby naturalne są 4-zgodne, jeżeli po zapisaniu ich w systemie o podstawie 4,
# zbiory cyfr występujące w liczbie są identyczne.

# Na przykład:
# 13 = 31(4) i 23 = 113(4)
# 18 = 102(4) i 33 = 201(4)
# 107 = 1223(4) i 57 = 321(4).

# Dana jest tablica T[N] zawierająca N liczb naturalnych.
# Proszę napisać funkcję, która zwraca długość najdłuższego podciągu (niekoniecznie spójnego) złożonego z liczb 4-zgodnych.

def najdluzszy_podciag_4zgodnych(T):
    def zbior_cyfr_w_systemie_czworkowym(liczba):
        """Funkcja zwraca krotkę, która reprezentuje obecność cyfr 0-3 w liczbie w systemie o podstawie 4."""
        cyfry = [0] * 4  # Tablica obecności cyfr 0, 1, 2, 3
        while liczba > 0:
            cyfry[liczba % 4] = 1  # Oznaczamy obecność cyfry
            liczba //= 4
        return tuple(cyfry)  # Konwertujemy na krotkę

    # Lista przechowująca grupy cyfr i ich liczność
    grupy = []  # Każdy element to [zbiór_cyfr, licznik]

    for liczba in T:
        zbior_cyfr = zbior_cyfr_w_systemie_czworkowym(liczba)
        # Sprawdzamy, czy taki zbiór cyfr już istnieje w grupach
        znaleziono = False
        for grupa in grupy:
            if grupa[0] == zbior_cyfr:  # Zbiór cyfr już istnieje
                grupa[1] += 1
                znaleziono = True
                break
        if not znaleziono:
            grupy.append([zbior_cyfr, 1])  # Dodaj nową grupę

    # Znajdujemy maksymalną liczność
    maks_dlugosc = max(grupa[1] for grupa in grupy)
    return maks_dlugosc


# Przykład użycia
T = [13, 23, 18, 33, 107, 57]
print(najdluzszy_podciag_4zgodnych(T))  # Wynik: 2
