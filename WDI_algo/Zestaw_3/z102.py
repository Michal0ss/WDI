# Dwie liczby naturalne są „przyjaciółkami jeżeli zbiory cyfr z których zbudowane są liczby
# są identyczne. Na przykład: 123 i 321, 211 i 122, 35 3553.

# Dana jest tablica T[N][N] wypełniona liczbami naturalnymi.
# Proszę napisać funkcję, która dla tablicy T zwraca ile elementów tablicy sąsiaduje wyłącznie z przyjaciółkami


def check_id_friends(x,n):
    count_x = [0]*10
    count_n = [0]*10

    while x>0:
        digit = x%10
        count_x[digit]+=1
        x//=10

    while n>0:
        digit = n%10
        count_n[digit]+=1
        n//=10

    if count_n==count_x:
        return True
    return False

def find_besties(t):
    n = len(t)
    count = 0

    def get_neighbours(i,j):
        neighbours = []
        if i > 0:
            neighbours.append(t[i-1][j]) # z dolu
        if i < n-1:
            neighbours.append(t[i+1][j]) # z gory
        if j > 0:
            neighbours.append(t[i][j-1]) # z lewej
        if j < n-1:
            neighbours.append(t[i][j+1]) # z prawej
        return neighbours

    for i in range(n):
        for j in range(n):
            neighbours = get_neighbours(i,j)
            all_friends = True

            for neighbour in neighbours:
                if not check_id_friends(t[i][j], neighbour):
                    all_friends = False
                    break

            if all_friends:
                count+=1
    return count