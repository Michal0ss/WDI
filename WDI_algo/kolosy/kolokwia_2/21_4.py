# ====================================================================================================>
# Zadanie 4, 16 grudnia 2021
# W tablicy o rozmiarze NxN wypełnionej liczbami naturalnymi umieszczono dokładnie jeden
# fragment ciągu Fiboacciego o długości co najmniej 3 elementów. Ciąg ten może leżeć w tablicy pionowo lub
# poziomo w kierunku rosnącym lub malejącym. Proszę napisać funkcje, która dla zadanej tablicy od szuka ten
# fragment i zwróci jego długość.
# 1 1 2 3 5
# 5 3 2 1 1
# ====================================================================================================>

def arr_is_fib(arr):
    n = len(arr)
    is_increasing = arr[0] < arr[1]

    for i in range(2, n):
        if is_increasing:  # Dla ciągu rosnącego
            if arr[i - 2] + arr[i - 1] != arr[i]:
                return False
        else:  # Dla ciągu malejącego
            if arr[i - 1] - arr[i] != arr[i - 2]:
                return False
    return True

def find_subseqs(t):
    n = len(t)
    max_length = 0
    # wiersze
    for i in range(n):
        for j in range(3,n+1):
            for k in range(n-j+1):
                row_subseq = t[i][k:k+j]
                if arr_is_fib(row_subseq):
                    max_length = max(max_length, len(row_subseq))

    #analogicznie kolumny
    for i in range(n):  # iterujemy po wierszac hlub kolumnach
        for j in range(3, n + 1): # dlugosc fragmentu
            for k in range(n - j + 1): # przesuwa po tablicy ten wycinek
                col_subseq = [t[x][i] for x in range(k,k+j)]
                if arr_is_fib(row_subseq):
                    max_length = max(max_length, len(col_subseq))

    return max_length
