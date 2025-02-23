
#Proszę znaleźć wyrazy początkowe ciągu zamiast 1,1 o najmniejszej sumie, aby w ciągu
#analogicznym do ciągu Fibonacciego wystąpił wyraz równy numerowi bieżącego roku.
target = 2024
min_sum = float('inf')
best_a, best_b = 0, 0

for a in range(1, 100):
    for b in range(1, 100):
        x, y = a, b
        while y < target:
            x, y = y, x + y
            if y == target:
                if a + b < min_sum:
                    min_sum = a + b
                    best_a, best_b = a, b
                break

print("Najmniejsze wartości początkowe to:", best_a, "i", best_b, "o sumie:", min_sum)
