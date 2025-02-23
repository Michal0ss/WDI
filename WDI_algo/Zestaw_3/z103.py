#Dana jest tablica T[N][N][N]. Proszę napisać funkcję, do której przekazujemy tablicę wypełnioną liczbami większymi od zera.
# Funkcja powinna zwracać wartość True, jeżeli na wszystkich poziomach tablicy liczba elementów sąsiadujących
#(w obrębia poziomu) z co najmniej 6 liczbami złożonymi jest jednakowa albo wartość False w przeciwnym przypadku.

def czy_liczba_sasiadow_jest_jednakowa(T):
    import math

    def czy_liczba_zlozona(x):
        """Sprawdza, czy liczba jest złożona."""
        if x < 2:
            return False
        for i in range(2, int(math.sqrt(x)) + 1):
            if x % i == 0:
                return True
        return False

    def liczba_sasiadow_zlozonych(tablica, x, y, z):
        """Zlicza sąsiadów złożonych na tym samym poziomie."""
        n = len(tablica)
        licznik = 0
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                if czy_liczba_zlozona(tablica[z][nx][ny]):
                    licznik += 1
        return licznik

    N = len(T)
    liczby_sasiadow = []

    for z in range(N):
        poziom_sasiadow = []
        for x in range(N):
            for y in range(N):
                if liczba_sasiadow_zlozonych(T, x, y, z) >= 6:
                    poziom_sasiadow.append((x, y))
        liczby_sasiadow.append(len(poziom_sasiadow))

    return len(set(liczby_sasiadow)) == 1
