# ====================================================================================================>
# Zadanie 172
# Proszęn apisać rekurencyjną funkcję obliczającą n-ty wyraz ciągu Fibonacciego ale tak aby
# wewnątrz funkcji było tylko jedno odwołanie rekurencyjne.
# ====================================================================================================>
# 0 1 1 2 3 5 8 13 21
def fibonacci(n, a=0, b=1):
    return fibonacci(n-1, b, b+a) if n>0 else a