# Dana jest plansza o wymiarach NxN zawierająca wartości 0 i 1. Pola o wartości 1 zawierają pułapki.
# Skoczek musi dotrzeć z górnego wiersza planszy do dolnego. Każdy ruch skoczka musi go przybliżać.

def can_knight_reach_bottom(board):
    """
    Funkcja sprawdza, czy skoczek szachowy może dotrzeć z górnego wiersza planszy (0, *)
    do dolnego wiersza (*, N-1), unikając pól z pułapkami (1).

    :param board: Tablica NxN zawierająca wartości 0 i 1
    :return: True, jeśli istnieje ścieżka, False w przeciwnym razie
    """
    N = len(board)

    # Ruchy skoczka: (delta_x, delta_y)
    knight_moves = [
        (-2, -1), (-1, -2), (1, -2), (2, -1),
        (2, 1), (1, 2), (-1, 2), (-2, 1)
    ]

    # Tablica odwiedzin
    visited = [[0 for _ in range(N)] for _ in range(N)]

    # Stos do przechowywania pozycji do odwiedzenia
    stack = []

    # Dodajemy wszystkie pola z górnego wiersza jako początkowe
    for j in range(N):
        if board[0][j] == 0:
            stack.append((0, j))
            visited[0][j] = 1

    # Przeszukiwanie
    while len(stack) > 0:
        current = stack[len(stack) - 1]  # Pobieramy ostatni element bez użycia pop
        stack = stack[:-1]  # Usuwamy ostatni element bez użycia pop
        x, y = current[0], current[1]

        # Sprawdzenie, czy dotarliśmy do dolnego wiersza
        if x == N - 1:
            return True

        # Przeglądanie możliwych ruchów skoczka
        for move in knight_moves:
            nx = x + move[0]
            ny = y + move[1]

            # Sprawdzenie, czy nowa pozycja jest w granicach planszy i nie zawiera pułapki
            if 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0 and visited[nx][ny] == 0:
                visited[nx][ny] = 1
                stack.append((nx, ny))
     
    return False

# Przykład użycia
board = [
    [0, 0, 1, 0],
    [1, 0, 1, 0],
    [0, 0, 0, 1],
    [1, 1, 0, 0]
]

result = can_knight_reach_bottom(board)
print("Czy skoczek może dotrzeć na dół?", result)
