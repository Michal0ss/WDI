# ====================================================================================================>
# Zadanie 166
# Dwie osoby otrzymały ten sam ciąg liter. Każda osoba pocięła go na kawałki i pomieszała.
# Proszę napisać program, który otrzymując dwa zbiory kawałków odtwarza napis początkowy jeżeli odtworzenie
# to jest jednoznaczne lub stwierdza brak możliwości jednoznacznego odtworzenia napisu. Na przykład
# dla zbiorów (1) ab,cde,cfed,fab (2) abc,abc,def,fed odtworzony napis to: abcdefabcfed
# ====================================================================================================>
# return string jak sie da lub return False jak sie nie da

#def split(t1):
#    nt1=[]
#    for fragment in t1:
#        nt1.extend(fragment)
#    return nt1


def rek(arr, next_t, right, word):
    """funkcja polega skleja napisy w taki sposób że szuka takiego napisu w tablicy, ktory zaczyna sie od
    ostatniio zakonczonego napisu drugiej.

    Ze znaleznionego napisu odcina poczatek i klei go z poprzednim

    Tworzy kopie tablicy bez danego napisu i wywołuje sie rekurencyjnie. Funkcja bedzie działac dopoki prawa czesc
    nie bedzie pusta lub nie znajdzie zadnego napisu zaczynajacego sie od tej prawej czesci np. abc i cde -> abcde
    lub abc i de -> None

    jesli ta prawa czesc zatem jest pusta oznacza to ze wykorzystalismy wszystkie wyrazy lub nie ma takiego napisu"""

    if right == "":
        return word if len(arr) ==0 else False

    for i, w in enumerate(arr):

        if w.startswith(right):
            new_t=arr[:i] + arr[i+1:]
            new_right = w[len(right):]

