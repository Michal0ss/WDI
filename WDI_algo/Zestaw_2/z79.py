# Dana jest N-elementowa tablica t zawierająca liczby naturalne mniejsze od 1000.
# Proszę napisać funkcję, która zwraca długość najdłuższego, spójnego fragmentu tablicy,
# dla którego w iloczynie jego elementów każdy czynniki pierwszy występuje co najwyżej raz.
# Na przykład dla tablicy t=[2,23,33,35,7,4,6,7,5,11,13,22] wynikiem jest wartość 5.

def prime_factors(num):
    factors = []
    divider = 2
    while divider**2<= num:
        while num % divider == 0:
            if divider not in factors:
                factors+=[divider]
            num//=divider
        divider += 1
    if num>= 1 and num not in factors:
        factors+=[num]
    return factors

def check_for_seq_factors(t):
    def all_unique_factors(subarray):
        overall_factors = []
        for num in subarray:
            factors = prime_factors(num)
            for factor in factors:
                if factor in overall_factors:
                    return False
                overall_factors+=[factor]
        return True

    n = len(t)
    max_length = 0
    for i in range(n):
        for j in range(i + 1, n + 1):
            if all_unique_factors(t[i:j]):
                current_len = j-i
                if current_len > max_length:
                    max_length=current_len
            else:
                break
    return max_length


t = [2, 23, 33, 35, 7, 4, 6, 7, 5, 11, 13, 22]
print(check_for_seq_factors(t))

