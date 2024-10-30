# Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
# naturalna jest palindromem, a następnie czy jest palindromem w systemie dwójkowym.


def bin(n):  # ZMIENIA NA DWOJKOWY

    eq=0
    position=1
    while n>0:
        eq += (n%2) * position
        n//=2
        position*=10
    return eq

def check_bin(n): # SPRAWDZA CZY DWOJKOWY JEST PALINDROMEM
    x = bin(n)
    original_x = x
    reversed_n=0
    while x>0:
        last_digit = x%10

        reversed_n = reversed_n*10 + last_digit

        x//=10

    return reversed_n == original_x


def palindrome(n): # SPRAWDZA CZY NORMALNY JEST PALINDROMEM

    original_n=n
    reversed_n=0
    while n>0:
        last_digit = n%10

        reversed_n = reversed_n*10 + last_digit

        n//=10 # usuwamy ostatnia cyfre z n

    return reversed_n == original_n


n = int(input("podaj palindrom fajny "))

print(palindrome(n), check_bin(n))