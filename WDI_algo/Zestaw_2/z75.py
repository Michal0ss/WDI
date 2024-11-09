# Mamy zdefiniowaną n-elementową tablicę liczb całkowitych. Proszę napisać funkcję zwracającą wartość typu bool oznaczającą,
# czy w tablicy istnieje dokładnie jeden element najmniejszy i dokładnie
# jeden element największy (liczba elementów najmniejszych oznacza liczbę takich elementów o tej samej
# wartości).

def insertion_sort(t):
    n=len(t)
    for i in range(1,n):
        key= t[i]
        j=i-1
        while j>=0 and t[j]>key:
            t[j+1]=t[j]
            j-=1
        t[j+1] = key
    return t

def find_min_and_max(t):
    sorted_t=insertion_sort(t)
    n=len(sorted_t)
    if sorted_t[0]!=sorted_t[1] and sorted_t[n-1]!=sorted_t[n-2]:
        return True
    return False



t=[123,123123123,112,2,31,3,13,1,31,5,94,7,4,3542365,63247327,3473623,326326,3262,33,4,4,25,325]
print(insertion_sort(t))
print(find_min_and_max(t))