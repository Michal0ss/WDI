def print_board(board):
    """Funkcja do wyświetlania planszy Sudoku."""
    for row in board:
        for num in row:
            if num == 0:
                print('.', end=' ')
            else:
                print(num, end=' ')
        print()

def is_valid(board, row, col, num):
    """Sprawdza, czy można umieścić liczbę w danym miejscu na planszy."""
    # Sprawdzenie wiersza
    if num in board[row]:
        return False

    # Sprawdzenie kolumny
    if num in (board[i][col] for i in range(9)):
        return False

    # Sprawdzenie kwadratu 3x3
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def solve_sudoku_recursive(board, row=0, col=0):
    """Rekurencyjne rozwiązanie Sudoku za pomocą algorytmu backtracking."""
    if row == 9:
        return True  # Osiągnięto koniec planszy

    if col == 9:
        return solve_sudoku_recursive(board, row + 1, 0)

    if board[row][col] != 0:
        return solve_sudoku_recursive(board, row, col + 1)

    for num in range(1, 10):
        if is_valid(board, row, col, num):
            board[row][col] = num

            if solve_sudoku_recursive(board, row, col + 1):
                return True

            board[row][col] = 0  # Cofnięcie (backtrack)

    return False

# Przykładowa plansza Sudoku (0 oznacza puste pole)
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9]
]

print("Plansza początkowa:")
print_board(sudoku_board)

if solve_sudoku_recursive(sudoku_board):
    print("\nRozwiązanie:")
    print_board(sudoku_board)
else:
    print("\nNie znaleziono rozwiązania.")
