#  Liczba doskonała to liczba równa sumie swoich podzielników właściwych (mniejszych od
# jej samej), na przykład 6 = 1 + 2 + 3. Proszę napisać program wyszukujący liczby doskonałe mniejsze od
# miliona.

def suma_dzielnikow_wlasciwych(n):
    suma = 1  # Zaczynamy od 1, bo 1 jest dzielnikiem każdej liczby
    # Sprawdzamy dzielniki od 2 do pierwiastka z n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            suma += i
            if i != n // i:  # Dodajemy także n // i, jeśli jest różne
                suma += n // i
    return suma

def liczby_doskonale(maks):
    # Sprawdzamy liczby od 2 do maks
    for n in range(2, maks):
        if suma_dzielnikow_wlasciwych(n) == n:
            print(n)  # Wypisujemy, jeśli liczba jest doskonała

# Wyszukiwanie liczb doskonałych mniejszych od miliona
maks = 1_000_000
print(f"Liczby doskonałe mniejsze od {maks}:")
liczby_doskonale(maks)