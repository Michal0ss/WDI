# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję,
# która odpowiada na pytanie, czy istnieje wiersz w tablicy w którym każda z liczb zawiera przynajmniej jedna cyfrę
# parzystą

def has_all_even_digits(num):
    """Sprawdza, czy liczba składa się wyłącznie z parzystych cyfr."""
    while num>0:
        digit = num%10
        if digit % 2 == 0:
            return True
        num//=10
    return False

def check_odd_digits_in_rows(T):
    k=0
    """Sprawdza, czy istnieje wiersz w tablicy w którym każda z liczb zawiera przynajmniej jedna cyfrę parzystą"""
    for row in T:
        found = True
        for num in row:
            if not has_all_even_digits(num):
                found = False
                break
        if found:
            return True
    return False

T = [
    [135, 246, 3527],
    [7377, 13, 893],
    [3323, 246, 5525]
]

print(check_odd_digits_in_rows(T))