#Dana jest tablica T[N][N] wypełniona liczbami całkowitymi. Proszę napisać funkcję, która
#wyszuka spójny podciąg elementów leżący poziomo lub pionowo o największej sumie. Maksymalna długość
#podciągu może wynosić 10 elementów. Do funkcji należy przekazać tablicę T, funkcja powinna zwrócić sumę
#maksymalnego podciągu.



def max_subarray_sum(t):
    n = len(t)
    max_sum = float('-inf')

    # Szukamy maksymalnej sumy w wierszach
    for i in range(n):
        for start in range(n):
            current_sum = 0
            for length in range(1, 11):  # Maksymalna długość podciągu to 10
                if start + length > n:
                    break
                current_sum += t[i][start + length - 1]
                max_sum = max(max_sum, current_sum)

    # Szukamy maksymalnej sumy w kolumnach
    for j in range(n):
        for start in range(n):
            current_sum = 0
            for length in range(1, 11):  # Maksymalna długość podciągu to 10
                if start + length > n:
                    break
                current_sum += t[start + length - 1][j]
                max_sum = max(max_sum, current_sum)
                
    return max_sum

# Przykład użycia
T = [
    [1, 2, -1, 4],
    [-2, 3, 0, 5],
    [4, -1, 2, 1],
    [1, 0, -3, 4]
]
print(max_subarray_sum(T))  # Wynik: Maksymalna suma podciągu
