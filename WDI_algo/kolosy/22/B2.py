# Dana jest kwadratowa tablica T wypełniona liczbami naturalnymi. Proszę napisać funkcję square(T), która
# znajdzie najmniejszy kwadratowy fragment tablicy, mniejszy niż cała tablica, taki że liczba będąca iloczynem
# czterech narożnych pól tego fragmentu w rozkładzie na czynniki pierwsze posiada tylko dwa różne czynniki.
# Funkcja powinna zwrócić rozmiar (bok) znalezionego kwadratu. Jeżeli kwadrat taki nie istnieje funkcja powinna zwrócić wartość 0.


def check_two_factors(m):
    temp = 0
    multiplier = 2
    while m>1:
        if m % multiplier == 0:
            temp+=1
            while m%multiplier == 0:
                m//=multiplier

            if temp == 2:
                return m ==1

        multiplier+=1

    return False

def square(t):
    n=len(t)
    for bok in range(1, n-1): # od 2x2 do najwiekszego:
        for w in range(n-bok):
            for k in range(n-bok):
                iloczyn = (t[w][k]*t[w][k+bok]*t[w+bok][k]*t[w+bok][(k+bok)])
                if check_two_factors(iloczyn):
                    return bok + 1
    return 0