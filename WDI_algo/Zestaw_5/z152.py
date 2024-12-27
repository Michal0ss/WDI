## ====================================================================================================>
# Zadanie 152
# Zadanie jak powyżej. Funkcja sprawdzająca czy król może dostać się z pola w,k do które-
# gokolwiek z narożników.
# ====================================================================================================>

def get_first_digit(num):
    while num > 9:
        num //= 10

    return num


def Zadanie_152(board: list, x, y):

    def rek(x, y, b: list, been=set()):
        been.add((x, y))

        if (
            x == 7
            and y == 7
            or x == 0
            and y == 7
            or x == 0
            and y == 0
            or x == 7
            and y == 0
        ):
            return True

        for x_n, y_n in (
            (x, y + 1),
            (x + 1, y + 1),
            (x + 1, y),
            (x + 1, y - 1),
            (x, y - 1),
            (x - 1, y - 1),
            (x - 1, y),
            (x - 1, y + 1),
        ):
            try:
                if not (x_n, y_n) in been:
                    firstd = get_first_digit(b[y_n][x_n])
                    if firstd > b[y][x] % 10:
                        if rek(x_n, y_n, b, been):
                            return True
            except IndexError:
                pass

        return False

    return rek(x, y, board)

t= [
                    [1, 4, 6, 2, 3, 5, 35, 2],
                    [1, 4, 6, 2, 3, 5, 35, 2],
                    [1, 4, 6, 82, 3, 5, 35, 2],
                    [1, 4, 6, 2, 3, 5, 35, 2],
                    [1, 4, 6, 2, 3, 5, 91, 2],
                    [1, 4, 6, 82, 3, 5, 24, 2],
                    [1, 4, 6, 2, 3, 5, 35, 7],
                    [1, 4, 6, 2, 3, 5, 35, 8],
                ]

print(Zadanie_152(t,1,1))