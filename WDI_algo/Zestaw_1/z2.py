# Proszę napisać program wypisujący elementy ciągu Fibonacciego mniejsze od miliona
# 1 1 2 3 5 8 13 21

a, b = 1, 1
while a<1_000_000:
    print(a)
    c=a+b
    a = b
    b=c