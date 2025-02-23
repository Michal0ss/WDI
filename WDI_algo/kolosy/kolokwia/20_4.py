# # ====================================================================================================>
# # Zadanie 168
# # Dana jest liczba naturalna N. Proszę zaimplementować funkcję divide(N), która sprawdza
# # czy jest możliwe pocięcie liczby N na kawałki, tak aby każdy z kawałków był liczba pierwszą oraz liczba kawał-
# # ków też była liczbą pierwszą. Funkcja powinna zwracać wartość logiczną. Naprzykład: divide(2347)=True,
# # podział na 23 i 47, natomiast divide(2255)=False.
# # Przykładowe wywołania funkcji:
# # print(divide(273)) # True, podział 2|7|3
# # print(divide(22222)) # True, podział 2|2|2|2|2
# # print(divide(23672)) # True, podział 23|67|2
# # print(divide(2222)) # False
# # print(divide(21722)) # False
# # ====================================================================================================>

def is_prime(num):
    if num <= 1:
        return False
    if num == 2 or num == 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False

    for i in range(6, int(num**0.5) + 3, 6):
        if num % (i + 1) == 0 or num % (i - 1) == 0:
            return False

    return True

def divide(N):
    def rek(num, nums,amount_slices, idx):
        # num to podstawowa liczba a nums to kawalki pociete amount slices to aktualna ilosc kawalkow
        if is_prime(num) and is_prime(amount_slices):
            return True
        if idx>num:
            return False

        if is_prime(num%idx):
            if rek(num//idx, [num%idx] + nums, amount_slices+1, 10):
                return True

        return rek(num, [*nums], amount_slices, idx*10)
    return rek(N,[], 1,10)