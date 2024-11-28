#Dana jest tablica T[N][N] wypełniona liczbami naturalnymi.
#Proszę napisać funkcję która zwraca wiersz i kolumnę dowolnego elementu,
#dla którego suma otaczających go elementów jest największa.

def find_biggest_sum(t):
    n = len(t)
    max_sum = -1
    best_position = (0,0)

    def get_neighbours(i, j):
        neighbours = []
        if i > 0:
            neighbours.append(t[i - 1][j])  # z góry
        if i < n - 1:
            neighbours.append(t[i + 1][j])  # z dołu
        if j > 0:
            neighbours.append(t[i][j - 1])  # z lewej
        if j < n - 1:
            neighbours.append(t[i][j + 1])  # z prawej
        return neighbours

    for i in range(n):
        for j in range(n):
            neighbours = get_neighbours(i, j)
            current_sum = 0
            for value in neighbours:
                current_sum += value
            if current_sum > max_sum:
                max_sum=current_sum
                best_position = (i,j)

    return best_position


t1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

t2 = [
    [0, 1, 0],
    [1, 10, 1],
    [0, 1, 0]
]

t3 = [
    [5, 5, 5],
    [5, 10, 9],
    [5, 5, 5]
]

print(find_biggest_sum(t1))  # Oczekiwany wynik: (1, 1)
print(find_biggest_sum(t2))  # Oczekiwany wynik: (1, 1)
print(find_biggest_sum(t3))