# Proszę napisać program obliczający i wypisujący stałą e z rozwinięcia w szereg e = 1/0! +
# 1/1! + 1/2! + 1/3! + ... z dokładnością N cyfr dziesiętnych (N jest rzędu 1000).
from shutil import which


def equation():
    e=1
    n=1
    w=1 # wartosc calego np. 1/2! itd
    while(w>0):
        e+=w
        n+=1
        w/=n
    return e

print(equation())