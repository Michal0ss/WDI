# Napisać program, który wyznacza n-tą cyfrę po przecinku rozwinięcia dziesiętnego wartości
# sqrt(2). Program powinien działać poprawnie dla n < 100

def nth_decimal_of_sqrt2(n):

    x = 1.5

    for _ in range(100):
        x=(x+2/x)/2

    decimal_part = x - int(x)

    decimals = []

    for _ in range(n):
        decimal_part *=10
        digit = int(decimal_part)
        decimals += [digit]
        decimal_part -= digit

    return decimals[n-1]

n = int(input("Podaj numer cyfry po przecinku: "))
if 1 <= n < 100:
    print(f"{n}-ta cyfra po przecinku sqrt(2) to: {nth_decimal_of_sqrt2(n)}")
else:
    print("Wprowadź wartość n w zakresie 1 ≤ n < 100.")
