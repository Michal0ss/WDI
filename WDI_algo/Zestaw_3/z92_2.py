import pprint

def spiral(T):
    """Wypełnia tablicę T liczbami naturalnymi w układzie spiralnym."""
    n = len(T)
    a = 0  # Liczba do wstawienia
    p, k = 0, n - 1  # Początkowe granice spiralnej iteracji

    while p <= k:
        # Góra (od lewej do prawej)
        for i in range(p, k + 1):
            a += 1
            T[p][i] = a
        # Prawa (z góry na dół)
        for i in range(p + 1, k + 1):
            a += 1
            T[i][k] = a
        # Dół (od prawej do lewej)
        for i in range(k - 1, p - 1, -1):
            a += 1
            T[k][i] = a
        # Lewa (z dołu do góry)
        for i in range(k - 1, p, -1):
            a += 1
            T[i][p] = a
        # Zacieśnij granice
        p += 1
        k -= 1

    return T
k, w = 5, 5  # Rozmiar tablicy
T = [[0 for _ in range(k)] for _ in range(w)]

result = spiral(T)
pprint.pprint(result)
