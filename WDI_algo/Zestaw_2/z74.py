# Dana jest duża tablica T. Proszę napisać funkcję, która zwraca informację czy w tablicy
# zachodzi następujący warunek: „wszystkie elementy, których indeks jest elementem ciągu Fibonacciego są
# liczbami złożonymi, a wśród pozostałych przynajmniej jedna jest liczbą pierwszą”

# [1,2,3,4,7,9,10,11,21] = len(9)
import math

def is_prime(n):
    if n<=1:
        return False
    if n==2 or n==3 or n==5:
        return True
    if n%5==0 or n%2 == 0 or  n%3==0:
        return False
    i=6

    for i in range(5, int(math.sqrt(n))+1, 6):
        if n%i==0 or n%(i+2)==0:
            return False

    return True


def find_by_fib_index(T):
    n=1
    while n<=len(T):
        if is_prime(T[n]):
            return False
        n=round(n*(1+5**0.5)/2)
    for i in T:
        if is_prime(i):
            return True
    return False

print(find_by_fib_index(T=[4,12,15,4,17,9,10,11,25,14,29,18,6,9,22]))