# ====================================================================================================>
# Zadanie 140
# Dany jest zestaw odważników T[N]. Napisać funkcję, która sprawdza czy jest możliwe
# odważenie określonej masy. Odważniki można umieszczać tylko na jednej szalce.
# ====================================================================================================>
# return bool

def weight(t, n, p=0):
    # t lista odwaznikow , n szukana waga, p numer brangeo odwaznika

    if n == 0:
        return True
    if p == len(t):
        return False
    return weight(t, n-t[p], p+1) or weight(t, n, p+1)

def zadanie_140(t,choosen_weight):
    return weight(t, choosen_weight)