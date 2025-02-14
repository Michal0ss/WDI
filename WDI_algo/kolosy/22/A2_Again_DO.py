# Dany jest ciąg 1, 2, 2, 3, 4, 6, 9, 14, 22, 35, ... (kolejny wyraz to suma dwóch poprzednich pomniejszona o 1).
# Dana jest kwadratowa tablica T wypełniona liczbami naturalnymi. W tablicy znajduje się jeden spójny
# fragment takiego ciągu o długości co najmniej 3 elementów. Wiadomo, że kolejne wyrazy tego fragmentu
# znalazły się w kolejnych kolumnach i jednocześnie w kolejnych wierszach tablicy. Proszę napisać funkcję
# seq(T), która znajdzie ten fragment w tablicy. Funkcja powinna zwrócić długość znalezionego fragmentu.

def check_subseq(arr):
    n=len(arr)
    for i in range(2,n):
        if arr[i]!=arr[i-2]+arr[i-1]-1:
            return False
    return True

def seq(t):
    n=len(t)
    for i in range(n):
        for j in range(n):
            ...
