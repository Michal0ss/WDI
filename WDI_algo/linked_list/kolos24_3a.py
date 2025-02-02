# Dany jest ciąg 𝑁 liczb naturalnych, z których wybieramy spójny fragment o długości 𝐾 (1 < 𝐾 < 𝑁).
# Pomiędzy wszystkie elementy wybranego fragmentu możemy wstawiać operatory dodawania albo
# mnożenia, tak aby powstało wyrażenie arytmetyczne. W powstałym wyrażeniu nie mogą wystąpić
# dwa jednakowe operatory obok siebie. Interesuje nas znalezienie takiego fragmentu ciągu, który
# pozwala zbudować wyrażenie o wartości będącej liczbą pierwszą, taką że stosunek tej liczby pierwszej
# do długości znalezionego fragmentu jest największy. Proszę napisać funkcję find_max(T), która dla
# ciągu zawartego w tablicy T, wyznaczy wartość maksymalnego ilorazu jaki można znaleźć. Jeżeli taki
# podciąg nie istnieje funkcja powinna zwrócić wartość zero.
# Na przykład dla ciągu: 7, 8, 6, 4, 7, 3 funkcja powinna zwrócić wartość 16.6.
# Możliwe podciągi dające liczby pierwsze to:
# 7 + 8 ⋅ 6 + 4 = 59, 59/4 = 14.75
# 7 + 8 ⋅ 6 + 4 ∗ 7 = 83, 83/5 = 16.6
# 6 ⋅ 4 + 7 = 31, 31/3 = 10.(3)
# 4 + 7 = 11, 11/2 = 5.5

from math import sqrt

def is_prime(n):
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


def find_max(t):
    pass

def create_variations(k,t):
    result_add_first = 0
    result_multiply_first = 0

    #pierwsze dodawniae
    result = t[0]
    for i in range(1,k):
        if i % 2 == 0:
            result += t[i-1]*t[i] # robimy to zeby istniała kolejnosc działan najpierw mnozymy potem dodajemy
    if k%2==0: # jesli ilosci cyfr jest podzielna przez dwa to dodajemy manualnie ostatni wyraz
        result += t[k-1]

    if is_prime(result):
        result_add_first = result/k

    #pierwsze mnozenie
    result = 0
    for i in range(k):
        if i%2==1:
            result += t[i-1]*t[i]
    if k%2==1:
        result +=t[k-1]

    if is_prime(result):
        result_multiply_first = result/k


    return max(result_add_first, result_multiply_first)

