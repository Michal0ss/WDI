#Wybieramy dodatnią liczbę całkowitą X. Z liczby X wykreślamy ostatnią cyfrę.
#Postępujemy tak, aż usuniemy wszystkie cyfry liczby X.
#Następnie sumujemy wszystkie powstałe w ten sposób liczby,
#włączając liczbę X. Na przykład, jeżeli wybraliśmy X = 1234 to w kolejnych krokach otrzymamy odpowiednio liczby 1234, 123, 12, 1.
#Ich suma to 1370. Mamy daną liczbę całkowitą dodatnią S.
#Proszę napisać program, który znajduje liczbę X taką, że powyżej opisana procedura daje sumę S.
#Można pokazać, że dla dowolnej dodatniej liczby S istnieje co najwyżej jedna taka wartość X.
# Jeżeli nie ma takiego X program powinien wypisać -1.

def pieces_sum(x):
    original_x = x
    s = x
    while x > 0:
        x //= 10
        s += x
    return s
def check_sum(s):
    for x in range(1, s + 1):
        if pieces_sum(x) == s:
            return x
    return -1

try:
    s = int(input("Podaj sumę: "))
    if s < 1:
        raise ValueError("Suma musi być liczbą całkowitą dodatnią.")

    result = check_sum(s)
    print(result)

except ValueError as e:
    print(f"Niepoprawna wartość: {e}")