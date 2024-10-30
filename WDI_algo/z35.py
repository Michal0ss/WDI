# Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
# ta zakończona jest unikalną cyfrą.

def check_last_digit(n):
    last_digit = n%10
    n//=10
    while n > 0:
        digit = n%10
        if digit == last_digit:
            return False
        n//=10
    return True

x=int(input(" podaj "))
print(check_last_digit(x))
