#Mając daną dodatnią liczbę całkowitą N , stwórzmy nową liczbę dodając kwadraty cyfr
#liczby N . Można udowodnić, że postępując w ten sposób wielokrotnie otrzymamy w końcu wynik 1 lub 4.
#Przykład: 13= 1 + 9 = 10 (Krok 1) 10 = 1 + 0 = 1 (Krok 2, kończymy iterację ponieważ
#uzyskaliśmy liczbę 1) Jeżeli w opisanej powyżej procedurze uzyskamy wynik 1, to liczbę N nazywamy “jednokwadratową”.
#Proszę napisać program, który znajduje K-tą liczbę w zadanym przedziale [L, U ], która jest
#jednocześnie jedno-kwadratowa i pierwsza


def length(x):
    counter = 0
    while x>0:
        x//=10
        counter+=1
    return counter

def sum_pow(x):
    x_len = length(x)
    digit_sum=0
    for i in range(x_len):
        digit= x%10
        digit_sum += digit**2
        x//=10
    return digit_sum

def main_algo(x):
    original_x = x
    while x>4:
        new_x= sum_pow(x)
        x=new_x
    return x

print(main_algo(19))