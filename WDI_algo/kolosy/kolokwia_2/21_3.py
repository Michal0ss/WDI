# ====================================================================================================>
# Zadanie 3, 16 grudnia 2021
# Na szachownicy o wymiarach NxN wypełnionej liczbami naturalnymi ¿1 odbywają się wyścigi wież.
# Pierwsza wieża startuje z lewego górnego rogu i ma dotrzeć do prawego dolnego rogu szachownicy.
# Pierwsza wieża może wykonywać tylko ruchy w prawo lub w dół szachownicy. Druga wieza startuje z prawego
# górnego rogu i ma dotrzeć do lewego dolnego rogu szachownicy. Druga wieża może wykonywać tylko ruchy w
# lewo lub w dół szachownicy. Wygrywa wieża, która dotrze do mety w mniejszej liczbie ruchów. Wieże mogą
# wykonać ruch z jednego pola na drugie tylko wtedy, gdy liczby na obu polach są względnie pierwsze. Proszę
# napisać funkcje,która dla danej tablicy zwraca numer wiezy, która wygra wyścig lub zero jeżeli wyścig będzie
# nierozstrzygnięty. Można założyć, ze podczas wyścigu wieże nie spotkają się na jednym polu
# ====================================================================================================>


def czy_wzgl_pierwsze(a,b):
    def nwd(a,b):
        while b:
            a,b=b,a%b
        return a
    return nwd(a,b)==1

def liczba_ruch(t,kierunek, start):
    n=len(t)

    def rek(x,y,ostatni_ruch):
        if x==n-1 and (y== n-1 or y ==0):
            return 0

        wartosc_ruch_dol = float("inf")
        if x+1<n and czy_wzgl_pierwsze(t[x][y], t[x+1][y]):
            wartosc_ruch_dol = rek(x+1,y,"dol")
            if ostatni_ruch != "dol":
                wartosc_ruch_dol+=1

        wartosc_ruch_bok = float("inf")
        if 0<=y+kierunek<n  and czy_wzgl_pierwsze(t[x][y], t[x][y+kierunek]):
        #poniewaz w dol dal obu wiez poruszamy sie identycznie jedyna rozniaca jest kierunek raz =-1 a raz =+1
            wartosc_ruch_bok = rek(x,y+kierunek,"bok")
            if ostatni_ruch!="bok":
                wartosc_ruch_bok+=1

        return min(wartosc_ruch_bok,wartosc_ruch_dol)
    return rek(start[0],start[1], None)

def main(t):
    rook1 = liczba_ruch(t,1,(0,0))
    rook2 = liczba_ruch(t, -1, (0, len(t)-1))

    if rook1 > rook2:
        return 2
    elif rook1 < rook2:
        return 1
    else:return 0

