# Napisać funkcję która dla tablicy T[N][N], wypełnionej liczbami całkowitymi, zwraca wartość True w przypadku,
# gdy w każdym wierszu i każdej kolumnie występuje co najmniej jedno 0 oraz wartość False w przeciwnym przypadku.

def check_column_for_0(t):
    """sprawdza czy w tablicy t w kazdej kolumnie wystepuje co najmniej jedno 0 """
    n=len(t)
    for i in range(n):
        found=False
        for j in range(n):
            if t[j][i] == 0:
                found=True
                break
        if not found:
            return False
    return True

def check_w_for_0(t):
    """sprawdza kazdy wiersz"""
    n = len(t)
    for i in range(n):
        found = False
        for j in range(n):
            if t[i][j] == 0:
                found = True
                break
        if not found:
            return False
    return True

def find_special_arr(t):
    """Sprawdza, czy w każdym wierszu i każdej kolumnie jest co najmniej jedno 0."""
    return check_column_for_0(t) and check_w_for_0(t)

# Przykład użycia
T = [
    [1, 0, 3],
    [4, 0, 6],
    [0, 8, 0]
]

print(find_special_arr(T))  # Wynik: True