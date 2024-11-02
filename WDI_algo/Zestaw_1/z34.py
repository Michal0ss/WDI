# Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy liczba
# ta zawiera cyfrę równą liczbie swoich cyfr


def check_amount_digits(n):
    original_n = n
    i=0
    while original_n>0:
        i += 1
        original_n//=10

    while n>0:
        digit=n%10
        if digit==i:
            return True
        n//=10
    return False

x = int(input(" podaj "))
print(check_amount_digits(x))