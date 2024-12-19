#Dana jest tablica T[N][N] wypełniona liczbami naturalnymi. Proszę napisać funkcję, która
#zwraca liczbę par elementów, o określonym iloczynie, takich że elementy są odległe o jeden ruch skoczka szachowego.

def count_pairs_product(t, target_multiplyp):

    n= len(t)

    knight_moves= [
        (-2,-1), (-2,1),
        (2, -1), (2, 1),
        (-1, 2), (1, -2),
        (-1, -2), (1, 2)
    ]

    count = 0

    for i in range(n):
        for j in range(n):

            for move in knight_moves:
                ni,nj = i+move[0], j+move[1]

                if 0<=ni < n and 0<= nj < n:
                    if t[i][j]*t[ni][nj] == target_multiplyp:
                        count +=1

    return count // 2

t = [
    [2,2,3],
    [5,5,6],
    [6,8,6]
]

product = 12
result = count_pairs_product(t, product)
print(f"pairs amount: {product}: {result}")