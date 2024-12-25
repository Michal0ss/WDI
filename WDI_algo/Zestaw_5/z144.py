# ====================================================================================================>
# Zadanie 144
# Dana jest tablica T[N]. Proszę napisać program zliczający liczbę “enek” o określonym
# iloczynie.
# ====================================================================================================>
# return liczba enek

def zadanie_144(t, product):
    def find_result_multiply(i, current_product)-> int:

        if current_product>product:
            return 0

        if i == len(t):
            return 1 if current_product == product else 0

        include_current = find_result_multiply(i+1, current_product *t[i])
        exclude_current = find_result_multiply(i+1, current_product)

        return include_current + exclude_current

    return find_result_multiply(0,1)

T = [2, 3, 2, 6]
target_product = 12
result = zadanie_144(T, target_product)
print("Liczba enek o iloczynie równym", target_product, "to:", result)