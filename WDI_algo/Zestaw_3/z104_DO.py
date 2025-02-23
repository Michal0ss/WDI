#Liczby naturalne a,b są komplementarne jeżeli ich suma jest liczbą pierwszą.
#Dana jest tablica T[N][N] wypełniona liczbami naturalnymi.
#Proszę napisać funkcję, która zeruje elementy nie posiadające liczby komplementarnej.
import math

def is_prime(x):
    if x<=1:
        return False
    for i in range(2,int(math.sqrt(x))+1):
        if x%i==0:
            return False
    return True

def find_complete_num():
    ...
