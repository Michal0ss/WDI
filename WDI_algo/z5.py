# Pierwiastek całkowitoliczbowy z liczby naturalnej to część całkowita z pierwiastka z tej liczby.
# Proszę napisać program obliczający taki pierwiastek korzystając z zależności 1 + 3 + 5 + ... = n^2

def integer_square_root(n):
    sum_of_odds = 0
    root = 0
    odd_num = 1

    while sum_of_odds<=n:
        sum_of_odds +=odd_num
        odd_num+=2  # Przechodzimy do kolejnej liczby nieparzystej
        root+=1 # dodajemy kolejne liczby nieparzyste i zapisujemy w ktorym indeksie jestesmy nieparzystych i jest to pierw
    return root - 1 # Jeśli przekroczyliśmy n, zmniejszamy root o 1, by uzyskać część całkowitą

n = 25
result = integer_square_root(n)
print("Pierwiastek całkowitoliczbowy z", n, "to:", result)