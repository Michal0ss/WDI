# funckaj znajdujaca zle przesnuieta mini tablice w suoku w wielkosci 3x3 i zwracajaca tuple z numerami tych kwadratow


def sudoku(t):
    def search(t):  # funkcja sprawdza czy w kazdym wierszu i kolumni powtarza sie cyfra
        for i in range(9):
            for j in range(9):
                for k in range(j,9):
                    if t[i][j]==t[i][k]: # sprawdza powtorzenia wierszu
                        return False
                    if t[j][i]==t[k][i]: # sprawdzic kolumny
                        return False
        return True
    def swap_squares(t,y1,x1,y2,x2): # zamiana miejscami mini tabele 3x3
        for i in range(3):
            for j in range(3):
                t[y1*3+i][x1*3+j] = t[y2*3+i][x2*3+j]
                t[y2 * 3 + i][x2 * 3 + j] = t[y1*3+i][x1*3+j]

    for y1 in range(3):
        for x1 in range(3):
            for y2 in range(3):
                for x2 in range(3):
                    swap_squares(t,y1,x1,y2,x2)
                    if search(t):
                        return y1*3+x1, y2*3+x2

t = [
    [3, 4, 5, 4, 5, 6, 7, 8, 9],
    [6, 7, 8, 7, 8, 9, 1, 2, 3],
    [9, 1, 2, 1, 2, 3, 4, 5, 6],
    [5, 6, 7, 3, 4, 5, 2, 3, 4],
    [8, 9, 1, 6, 7, 8, 8, 9, 1],
    [2, 3, 4, 9, 1, 2, 5, 6, 7],
    [1, 2, 3, 6, 7, 8, 9, 1, 2],
    [4, 5, 6, 9, 1, 2, 3, 4, 5],
    [7, 8, 9, 3, 4, 5, 6, 7, 8]
]


print(sudoku(t))