# Dane są dwie tablice mogące pomieścić taką samą liczbę elementów: T1[N][N] i T2[M], gdzie
# M=N*N. W każdym wierszu tablicy T1 znajdują się uporządkowane niemalejąco (w obrębie wiersza) liczby
# naturalne. Proszę napisać funkcję przepisującą wszystkie liczby z tablicy T1 do T2, tak aby liczby w tablicy
# T2 były uporządkowane niemalejąco
from heapq import merge


def translate_arr(t1,t2):
    merged = []
    i,j=0,0
    n=len(t1)
    m=len(t2)
    while i < n and j<m:
        print(i,j)
        if t1[i]<= t2[j]:
            merged.append(t1[i])
            i+=1
        else:
            merged.append(t2[j])
            j+=1

    while i<n:
        merged.append(t1[i])
        i+=1
    while j<m:
        merged.append(t2[j])
        j+=1
    return merged

def translate_and_sort(T1):
    n=len(T1)
    t2=T1[0]

    for i in range(1,n):
        t2 = translate_arr(t2, T1[i])

    return t2

T1 = [
    [1, 3, 5],
    [2, 4, 6],
    [7, 8, 9]
]


result = translate_and_sort(T1)
print("Posortowana tablica T2:", result)
