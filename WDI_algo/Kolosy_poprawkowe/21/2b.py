# Aby otrzymać nagrodę trzeba przejść kolejno przez N komnat. W każdej komnacie znajduje się
# skrzynia (mogąca pomieścić maksymalnie 100 sztabek), w której umieszczono pewną liczbę sztabek
# złota. Będąc w danej komnacie możemy zabrać ze skrzyni pewną liczbę sztabek albo dołożyć do
# skrzyni wcześniej zebrane sztabki. Liczba sztabek przenoszona do następnej komnaty nie może
# przekraczać 6. Drzwi do kolejnej komnaty otwierają się wtedy, gdy liczba sztabek pozostawiona
# w skrzyni będzie liczbą pierwszą. Z ostatniej komnaty nie wolno wynieść żadnej sztabki. Proszę
# napisać funkcję, która zwraca informację, czy jest możliwe przejście przez komanty. Do funkcji
# należy przekazać tablicę zawierającą liczby sztabek w kolejnych komnatach. Na przykład:
# T = [10, 20, 30] −→ funkcja powinna zwrócić False
# T = [10, 20, 35] −→ funkcja powinna zwrócić True, w komnatach pozostanie [5, 23, 37]

def is_prime(n):
    """Sprawdza, czy liczba n jest pierwsza."""
    if n < 2:
        return False
    if n in (2, 3):
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def prize(t):
    n = len(t)

    def rek(idx, amount_gold):

        if idx == n - 1 and is_prime(t[idx]) and amount_gold == 0:
            return True


        if idx >= n:
            return False

        for take in range(min(6, t[idx]) + 1):  # Możemy zabrać od 0 do 6 sztabek (lub tyle, ile jest)
            for put in range(min(6, amount_gold) + 1):  # Możemy dołożyć od 0 do 6 sztabek (lub tyle, ile mamy)
                new_gold = amount_gold + take - put  # logika przenoszenia sztabek
                new_sztabki = t[idx] - take + put  # Nowa liczba sztabek w komnacie po operacji


                if new_gold <= 6 and new_sztabki <= 100 and is_prime(new_sztabki):
                    t[idx] = new_sztabki

                    if rek(idx + 1, new_gold):
                        return True

                    t[idx] = t[idx] + take - put  # (backtracking)

        return False

    return rek(0, 0)

# Przykłady testowe:
print(prize([10, 20, 30]))  # False
print(prize([10, 20, 35]))  # True
print(prize([4, 6, 5]))     # True
print(prize([9, 10, 15]))   # False
