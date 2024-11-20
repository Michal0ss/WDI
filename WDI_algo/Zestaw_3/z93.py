# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
# odpowiada na pytanie, czy w każdym wierszu tablicy występuje co najmniej jedna liczba złożona wyłącznie
# z nieparzystych cyfr


def has_all_odd_digits(num):
    """Sprawdza, czy liczba składa się wyłącznie z nieparzystych cyfr."""
    while num>0:
        digit = num%10
        if digit % 2 == 0:
            return False
        num//=10
    return True

def check_odd_digits_in_rows(T):
    """Sprawdza, czy w każdym wierszu tablicy T istnieje liczba składająca się wyłącznie z nieparzystych cyfr."""
    for row in T:
        found = False
        for num in row:
            if has_all_odd_digits(num):
                found = True
                break
        if not found:
            return False
    return True

T = [
    [135, 246, 3527],
    [7277, 13, 890],
    [325, 246, 135]
]

print(check_odd_digits_in_rows(T))