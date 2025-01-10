# ====================================================================================================>
# Zadanie 170
# Dana jest funkcja Ackermana, określona na zbiorze liczb całkowitych nieujemnych, dana
# wzorem rekurencyjnym:
# def f(a,b):
#    if a==0:
#       return b+1
#    if b==0:
#       return f(a-1,1)
#    return f (a-1,f(a,b-1))
# Proszę napisać funkcję w wersji iteracyjnej.
# ====================================================================================================>

def ackerman(a,b):
    stos = [a,b]

    while len(stos)>1:
        b,a = stos.pop(), stos.pop() # usuwa ostatni element tablicy i przypisuje do a i b

        if a ==0:
            stos.append(b+1)
        elif b==0:
            stos.append(a-1)
            stos.append(1)
        else:
            stos.append(a-1)
            stos.append(a)
            stos.append(b-1)
            print(a,b)
    return stos[0]

print(ackerman(2, 3))  # Wynik: 9
print(ackerman(3, 2))  # Wynik: 29
