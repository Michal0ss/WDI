# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
# zwraca wiersz i kolumnę dowolnego elementu, dla którego iloraz sumy elementów w kolumnie w którym leży
# element do sumy elementów wiersza w którym leży element jest największa.

# Poprzednie zadanie z tablicą wypełnioną liczbami całkowitymi.

def find_max_ratio_position(t):
    """Znajduje wiersz i kolumnę elementu o największym ilorazie sumy kolumny do sumy wiersza."""

    n=len(t)
    max_ratio=0
    result_row, result_col = -1,-1

    for row in range(n):
        row_sum=0
        for j in range(n):
            row_sum+=t[row][j] # suma wierszy

        for col in range(n):
            col_sum=0
            for i in range(n):
                col_sum+=t[i][col] # suma kolumny

                if row_sum !=0: # kolumny do wierszy -> k/w
                    ratio=col_sum/row_sum
                    if ratio>max_ratio:
                        max_ratio = ratio
                        result_row,result_col = row, col


    return result_row,result_col

T = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

row, col = find_max_ratio_position(T)
print(f"Największy iloraz znajduje się w wierszu {row}, kolumnie {col}.")
