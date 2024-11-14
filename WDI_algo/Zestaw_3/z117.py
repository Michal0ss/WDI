# W tablicy o rozmiarze NxN wypełnionej liczbami naturalnymi umieszczono dokładnie jeden
# fragment ciągu Fiboacciego o długości co najmniej 3 elementów. Ciąg ten może leżeć w tablicy pionowo lub
# poziomo w kierunku rosnącym lub malejącym. Proszę napisać funkcje, która dla zadanej tablicy odszuka ten
# fragment i zwróci jego długość

def is_fib(x,y):
    a,b=0,1
    while a<x and y<b:
        if a==x and b==y:
            return True
        else:
            a,b=b,a+b
    return False

def fib_seq(T):
    n=len(T)
    for w in range(n-2):
        for k in range(n-2):
            a = T[w][k]
            b = T[w+1][k+1]
            c = T[w+2][k+2]
            if a<=b and c==a+b:
                if is_fib((a,b)):
                    max_l = 3
                    while w+3<n and k+3 <n:
                        a,b,c=b,c,T[w+3][k+3]
                        w+=1
                        k+=1
                        if c!=a+b:
                            return max_l
                        max_l+=1
                    return max_l
