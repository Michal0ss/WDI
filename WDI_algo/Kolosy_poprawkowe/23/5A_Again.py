# Dana jest kwadratowa tablica T wypełniona liczbami naturalnymi. Proszę napisać funkcję square(T),
# która znajdzie w tablicy największy kwadrat, złożony wyłącznie z elementów,
# które w zapisie ósemkowym złożone są z niepowtarzających się cyfr.
# Do funkcji należy przekazać tablicę, funkcja powinna zwrócić długość boku znalezionego kwadratu.
# Kwadrat 1 × 1 też jest kwadratem. W przypadku nieznalezienia żadnego kwadratu należy zwrócić wartość 0.
# Dane wejściowe w tablicy mają pozostać niezniszczone.

from math import log10

def eight(n):
    tab=[0,0,0,0,0,0,0,0]
    while n>0:
        div = n%8
        tab[div]+=1
        if tab[div]>1:
            return False
        n=n//8
    return True

def is_proper(t,i,j,k): # k to dlugosc boku
    for row in range(i,i+k):
        for col in range(j,j+k):
            if not eight(t[row][col]):
                return False
    return True
def square(T):
    maxi=0
    for i in range(len(T)):
        for j in range(len(T)):
            for k in range(len(T)-max(i,j)):
                maxi = max(maxi,k)
        if i > len(T)-maxi:
            return maxi
    return maxi