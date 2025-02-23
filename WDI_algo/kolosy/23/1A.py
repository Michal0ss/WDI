# Dwie liczby naturalne większe od 1 są zgodne jeżeli dzielą się przez te same liczby pierwsze.
# Przykładem zgodnych liczb są pary: (6, 24),(40, 50),(13, 169),(44, 242), nie są zgodne np. pary:
# (6, 8),(40, 60),(13, 39),(44, 99).

# Tablica 𝑇 została wypełniona liczbami z zakresu [2..999]. Sąsiadami pola o indeksie 𝑖 w
# tablicy są pola o indeksie 𝑗, gdy 𝑎𝑏𝑠(𝑖 − 𝑗) < 3. Proszę napisać funkcję zgodne(T), która dla
# tak wypełnionej tablicy zwraca liczbę elementów mających przynajmniej jednego zgodnego sąsiada.
# Po wykonaniu funkcji tablica nie musi pozostać nie zmieniona. Na przykład dla tablicy:

# 𝑇 = [2, 3, 4, 5, 7, 6, 23, 24, 12, 13, 14, 15, 16, 45] funkcja powinna zwrócić wartość 7 (są to liczby
# 2, 4, 6, 24, 12, 15, 45).

def weryf(a,b):
    d=2

    while a>1 and b>1:
        if a%d == 0 and b%d == 0:
            while a%d==0:
                a//=d
            while b%d==0:
                b//=d

        if a%d==0 or b%d==0:
            return False
        d+=1

        if a>1 or b>1:
            return False
    return True

def zgodne(t:list[int]):
    l = len(t)
    if l<2:
        return 0
    pom = [0]*l



