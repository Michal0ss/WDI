# Liczbę pierwszą będącą palindromem nazywamy “palindromem pierwszym”.
# Liczbę nazywamy “super palindromem pierwszym” jeżeli podczas odrzucania parami skrajnych cyfr do końca pozostaje ona palindromem pierwszym.
# Na przykład, liczba 373929373 jest super palindromem pierwszym bo 373929373, 7392937, 39293, 929, 2 są palindromami pierwszymi.
# Początkowymi super palindromami pierwszymi są: 2, 3, 5, 7, 11, 131, 151.
# Proszę napisać program, który wylicza ile jest super palindromów pierwszych
# mniejszych od zadanej liczby n

def find_palindrome(x):

    original_x=x
    reversed_x=0
    while x > 0:
        last_digit = x%10

        reversed_x = (reversed_x*10)+last_digit

        x//=10


    return reversed_x==original_x

def perfect_palindrome(x):
    count = 0
    for i in range (2,x+1):
        find_palindrome(i)
        count+=1
    return count

print(perfect_palindrome(160))