# Proszę napisać program sprawdzający czy istnieje spójny podciąg ciągu Fibonacciego o zadanej sumie.

def fibo_check(x):
    a, b = 1, 1  # Inicjalizacja pierwszych dwóch liczb Fibonacciego
    left_a, left_b = 1, 1  # Inicjalizacja wskaźników lewych
    current_sum = 0

    while b <= x:

        current_sum += b
        print(current_sum)  # Generowanie i sprawdzanie liczb Fibonacciego dopóki są mniejsze lub równe x
        print()
        # Sprawdzanie, czy suma przekroczyła x i korygowanie wskaźników lewych
        while current_sum > x:
            print(current_sum+1)
            current_sum -= left_a
            temp = left_a + left_b  # Obliczenie nowej wartości lewej granicy
            left_a = left_b
            left_b = temp

        # Sprawdzenie, czy aktualna suma jest równa x
        if current_sum == x:
            return True

        # Generowanie kolejnej liczby Fibonacciego
        temp =a+b
        a=b
        b=temp

    return False


# Main part
y = int(input("Podaj naturalną sumę podciągu Fibonacciego: "))
if fibo_check(y):
    print(f"Istnieje spójny podciąg ciągu Fibonacciego o sumie {y}.")
else:
    print(f"Nie istnieje spójny podciąg ciągu Fibonacciego o sumie {y}.")