# Pewne liczby pierwsze są palindromami i pozostają liczbami pierwszymi pomimo pozbawiania ich skrajnych cyfr.
# Na przykład: 71317 → 131 → 3. Proszę napisać program, który wypisuje wszystkie takie
# liczby mniejsze od N.

def find_palindromes(n):

    original_n = n
    reversed_n = 0
    while n>0:
        print(n)
        print("----")
        print(reversed_n)
    # pobieramy ostatnia cyfe
        last_digit=n%10
    # mnozymy razy 10 i dodajemy liczbe do odwroconej
        reversed_n = reversed_n* 10 + last_digit
    # Usuwamy ostatnią cyfrę z oryginalnej liczby
        n//=10
    return original_n == reversed_n

print(find_palindromes(12321))