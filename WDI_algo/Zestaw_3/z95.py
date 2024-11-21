# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
# zwraca wiersz i kolumnę dowolnego elementu, dla którego iloraz sumy elementów w kolumnie w którym leży
# element do sumy elementów wiersza w którym leży element jest największa.

def find_max_ratio_position(t):
    """Znajduje wiersz i kolumnę elementu o największym ilorazie sumy kolumny do sumy wiersza."""

    n=len(t)
    max_licz = -1
    #Ustawiamy go na bardzo małą wartość, aby każda pierwsza obliczona wartość ilorazu była większa i nadpisała tę wartość.
    max_mian = 1
    result_row, result_col = -1,-1

    for row in range(n):
        row_sum=0
        for j in range(n):
            row_sum+=t[row][j]

        for col in range(n):
            col_sum=0
            for i in range(n):
                col_sum+=t[i][col]

            if row_sum>0:
                if col_sum*max_mian>max_licz*row_sum:
                    max_licz = col_sum
                    max_mian = row_sum
                    result_row,result_col = row,col

    return result_row,result_col


T = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

row, col = find_max_ratio_position(T)
print(f"Największy iloraz znajduje się w wierszu {row}, kolumnie {col}.")
