# Napisać program wypełniający N-elementową tablicę T
# liczbami naturalnymi 1-1000 i sprawdzający czy każdy element tablicy zawiera co najmniej jedną cyfrę nieparzystą.

def check(x):
    while x>0:
        digit = x%10
        if digit%2!=0:
            return True
        x//=10
    return False

def check_odd_digit():
    T = []  # Inicjalizacja pustej listy
    i = 1

    while i <= 1000:
        T.append(i)
        i += 1

    T = [i for i in T if check(i)]

    print(T)
    return T

check_odd_digit()