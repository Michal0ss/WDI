# Dana jest kwadratowa tablica T wypełniona liczbami naturalnymi. Proszę napisać funkcję square(T), która
# znajdzie najmniejszy kwadratowy fragment tablicy, mniejszy niż cała tablica, taki że liczba będąca iloczynem
# czterech narożnych pól tego fragmentu w rozkładzie na czynniki pierwsze posiada tylko dwa różne czynniki.
# Funkcja powinna zwrócić rozmiar (bok) znalezionego kwadratu.
# Jeżeli kwadrat taki nie istnieje funkcja powinna zwrócić wartość 0

def diffrent_factors(multiply):
    res = 0
    dzielnik = 2
    while multiply>1:
        if multiply%dzielnik==0:
            res+=1
            while multiply%dzielnik==0:
                multiply//=dzielnik

            if res == 2:
                return multiply == 1

    return False




def find_squares(t):
    n = len(t)
    for bok in range(1,n-1):
        for wiersz in range(n-bok):
            for kolumna in range(n-bok):
                iloczyn = t[wiersz][kolumna]*t[wiersz][kolumna+bok]*t[wiersz+bok][kolumna+bok]
                if diffrent_factors(iloczyn):
                    return bok+1
    return 0

