# ====================================================================================================>
# Zadanie 145
# Proszę zmodyfikować poprzedni program aby wypisywał znalezione n-ki.
# ====================================================================================================>
# Dla [1, 2, 3, 4, 5, 6], 6 wynik to '[1, 2, 3]\n[1, 6]\n[2, 3]' kolejnosci printowania nie ma znaczenia
from sympy.physics.units import current


def zadanie_144(t, product):
    def find_result_multiply(i, current_product, subset):

        if current_product>product:
            return []

        if i == len(t):
            if current_product == product:
                return [subset] if len(subset)>1 else []
            return []

        include_current = find_result_multiply(i+1, current_product *t[i], subset + [t[i]])
        exclude_current = find_result_multiply(i+1, current_product, subset)

        return include_current + exclude_current

    return find_result_multiply(0,1,[])

T = [1, 2, 3, 4, 5, 6]
target_product = 6
result = zadanie_144(T, target_product)
print("Liczba enek o iloczynie równym", target_product, "to:", result)