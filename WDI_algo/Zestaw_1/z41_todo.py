# Napisać program, który wyznacza ostatnia niezerową cyfrę liczby N!. Program powinien
# działać dla N rzędu 10^100
def last_nonzero_digit_of_factorial(N):
    result = 1
    count_2 = 0
    count_5 = 0

    for i in range(1, N + 1):
        current = i

        # Usuwamy czynniki 2 z current i zliczamy ich liczbę
        while current % 2 == 0:
            current //= 2
            count_2 += 1

        # Usuwamy czynniki 5 z current i zliczamy ich liczbę
        while current % 5 == 0:
            current //= 5
            count_5 += 1

        # Mnożymy pozostały current do wyniku
        result = (result * current) % 10

    # Zbilansowanie nadmiaru czynników 2 (pozostaje tylko tyle, ile brakujących 5)
    for _ in range(count_2 - count_5):
        result = (result * 2) % 10

    return result

# Przykład użycia
if __name__ == "__main__":
    N = int(input("Podaj N: "))
    print("Ostatnia niezerowa cyfra {}!: {}".format(N, last_nonzero_digit_of_factorial(N)))
