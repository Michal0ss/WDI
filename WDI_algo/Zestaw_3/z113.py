#Dana jest tablica T[N][N] wypełniona wartościami 0, 1. Każdy wiersz tablicy traktujemy
#jako liczbę zapisaną w systemie dwójkowym o długości N bitów. Stała N jest rzędu 1000.
#Proszę zaimplementować funkcję distance(T), która dla takiej tablicy wyznaczy dwa wiersze,
#dla których różnica zawartych w wierszach liczb jest największa.
#Do funkcji należy przekazać tablicę, funkcja powinna zwrócić odległość pomiędzy znalezionymi wierszami.
#Można założyć, że żadne dwa wiersze nie zawierają identycznego ciągu cyfr.

#def decimal_to_binary(x):
#    binary = 0
#    power_of_two = 1
#
#    # Find the largest power of two less than or equal to x
#    while power_of_two <= x:
#        power_of_two *= 2
#    power_of_two //= 2  # Go back to the largest fitting power of two
#
#    # Build the binary result
#    while power_of_two > 0:
#        if x >= power_of_two:
#            binary = binary * 10 + 1  # Add 1 to the binary number
#            x -= power_of_two
#        else:
#            binary = binary * 10  # Add 0 to the binary number
#        power_of_two //= 2
#
#    return binary
#
#def connect_raw(t):
#    n= len(t)
#    s=0
#    for i in range(n):
#        s += t[i]*(10^(n-1-i))
#    return s
#
#def distance(t, n=1000):
#    T = []
#    rows = [row for row in t]
#    for i in range(n):
#        T.append(decimal_to_binary(connect_raw(rows[i])))
#
#    max_dif = float('-inf')
#    for j in range(n):
#        for k in range(j+1,n):
#            current_dif = T[j]-T[k]
#            if max_dif>current_dif:
#                max_dif=current_dif
#    return max_dif


def distance(T):
    N = len(T)  # Rozmiar tablicy
    max_diff = 0  # Inicjalizujemy maksymalną różnicę jako 0

    # Przekształcenie wierszy tablicy T na liczby całkowite
    rows = []
    for row in T:
        num = 0
        for bit in row:
            num = num * 2 + bit  # Dodajemy bit do liczby binarnej
        rows.append(num)

    # Szukanie dwóch wierszy o największej różnicy
    for i in range(N):
        for j in range(i + 1, N):
            diff = abs(rows[i] - rows[j])  # Obliczamy różnicę
            if diff > max_diff:
                max_diff = diff  # Aktualizujemy maksymalną różnicę

    return max_diff

T = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 1, 1]
]

print(distance(T))  # Wynik: 6

# [1,0,1,0,0]