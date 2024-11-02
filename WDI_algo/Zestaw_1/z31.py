# proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
# na jest wielokrotnością dowolnego wyrazu ciągu danego wzorem An = 3 ∗ An−1 + 1, a pierwszy wyraz jest
# równy 2.

# an=3*2+1
def is_multiply_of_sequence(n):
    a=2
    while True:
        an = 3 * a + 1
        if an>n:
            break
        if n%an==0:
            return True
        a=an
    return False


n = int(input("Podaj liczbe naturalna: "))

if n > 0:
    if is_multiply_of_sequence(n):
        print(f"Liczba {n} jest wielokrotnością przynajmniej jednego wyrazu ciągu An = 3 ∗ An−1 + 1.")
    else:
        print(f"Liczba {n} nie jest wielokrotnością żadnego wyrazu ciągu An = 3 ∗ An−1 + 1.")
else:
    raise ValueError("Liczba musi być naturalna (większa od zera).")