# Na szachownicy o wymiarach NxN wypełnionej liczbami naturalnym ¿1 odbywają się wyścigi wież.
# Pierwsza wieża startuje z lewego górnego rogu i ma dotrzeć do prawego dolnego rogu szachownicy.
# Pierwsza wieża może wykonywać tylko ruchy w prawo lub w dół szachownicy. Druga wie¿a startuje z prawego
# górnego rogu i ma dotrzeć do lewego dolnego rogu szachownicy. Druga wieża może wykonywać tylko ruchy w
# lewo lub w dół szachownicy. Wygrywa wieża, która dotrze do mety w mniejszej liczbie ruchów. Wieże mogą
# wykonać ruch z jednego pola na drugie tylko wtedy, gdy liczby na obu polach są względnie pierwsze. Proszę
# napisać funkcjˆe, która dla danej tablicy zwraca numer wie¿y, która wygra wyścig lub zero jeżeli wyścig będzie
# nierozstrzygnięty. Można założyć, ¿e podczas wyścigu wieże nie spotkają się na jednym polu


def nwd(a,b):
    while b!=0:
        temp = b
        b= a%b
        a= temp
    return abs(a)

def move_rook(start, end, moves, t):
    n = len(t)
    queue = [(start[0], start[1], 0)] # x, y, liczba ruchow
    visited = set()
    visited.add((start[0], start[1]))

    while queue:
        x, y, steps = queue.pop(0)
        if (x,y)==end:
            return steps

        for dx, dy in moves:
            nx, ny = x+ dx, y + dy
            if 0<= nx < n and 0<= ny < n and (nx,ny) not in visited:
                if nwd(t[x][y], t[nx][ny]) == 1:
                    visited.add((nx, ny))
                    queue.append((nx,ny, steps + 1))
    return -1

def rook_race(t):
    """
        Określa, która wieża wygrywa wyścig.
        Zwraca:
        - 1: jeśli wygrywa pierwsza wieża
        - 2: jeśli wygrywa druga wieża
        - 0: jeśli wyścig jest nierozstrzygnięty
        """
    n = len(t)

    moves_1 = [(0, 1),(1, 0)] # prawo dol
    moves_2 = [(0, -1), (1, 0)] # lewo, dol

    start_1, end1 = (0,0), (n-1, n-1)
    start_2, end2 = (0, n-1), (n - 1, 0)

    result1 = move_rook(start_1, end1, moves_1,t)
    result2 = move_rook(start_2, end2, moves_2,t)

    if result1 < result2:
        return 1
    if result1>result2:
        return 2
    else:
        return 0

szachownica = [
    [2, 3, 5],
    [7, 11, 13],
    [17, 19, 23]
]


print(rook_race(szachownica))