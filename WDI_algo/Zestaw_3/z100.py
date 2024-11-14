# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
# w poszukuje w tablicy kwadratu o liczbie pól będącej liczbą nieparzystą większą od 1, którego iloczyn 4 pól
# narożnych wynosi k. Do funkcji należy przekazać tablicę i wartość k. Funkcja powinna zwrócić informacje
# czy udało się znaleźć kwadrat oraz współrzędne (wiersz, kolumna) środka kwadratu


def znajdz_kwadrat(T, k):
    N = len(T)

    # Rozmiar kwadratu zaczyna się od 3 i zwiększa o 2 (bo tylko nieparzyste)
    for n in range(3, N + 1, 2):
        r = (n - 1) // 2

        # Przeglądaj każdy możliwy środek kwadratu o rozmiarze n x n
        for i in range(r, N - r):
            for j in range(r, N - r):
                # Wyznaczamy narożne pozycje
                lewy_gorny = T[i - r][j - r]
                prawy_gorny = T[i - r][j + r]
                lewy_dolny = T[i + r][j - r]
                prawy_dolny = T[i + r][j + r]

                # Obliczamy iloczyn narożników
                iloczyn_naroznikow = lewy_gorny * prawy_gorny * lewy_dolny * prawy_dolny

                # Sprawdzamy, czy iloczyn wynosi k
                if iloczyn_naroznikow == k:
                    return True, (i, j)  # Zwracamy True i współrzędne środka kwadratu

    # Jeśli nie znaleziono takiego kwadratu, zwracamy False
    return False, None
