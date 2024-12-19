#Dana jest tablica T[N][N] (reprezentująca szachownicę) wypełniona liczbami naturalnymi.
#Proszę napisać funkcję która ustawia na szachownicy dwie wieże, tak aby suma liczb na „szachowanych”
#przez wieże polach była największa. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić położenie
#wież. Uwaga- zakładamy, że wieża szachuje cały wiersz i kolumnę z wyłączeniem pola na którym stoi

def find_optimal_loc(t):
    n = len(t)

    w_sum = [0 for _ in range(n)]
    k_sum = [0 for _ in range(n)]

    for i in range(n):
        for j in range(n):
            w_sum[i] += t[i][j]
            k_sum[j] += t[i][j]

    max_sum = 0
    best_positions = None

    for w1 in range(n):
        for k1 in range(n):
            sum1 = w_sum[w1] + k_sum[k1] - t[w1][k1]

            for w2 in range(n):
                for k2 in range(n):
                    if w1 == w2 or k1 == k2:
                        continue
                    sum2 = w_sum[w2] + k_sum[k2] - t[w1][k1]

                    total_sum = sum1 + sum2 - t[w1][k2] - t[w2][k1] # odjecie podwojnie policzonych pol szachownicy
                                                                    # ( przeciecia szachowanych pol )

                    if total_sum > max_sum:
                        max_sum = total_sum
                        best_positions = [(w1,k1),(w2,k2)]

    return best_positions

T = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = find_optimal_loc(T)
print("Najlepsze pozycje wież:", result)
