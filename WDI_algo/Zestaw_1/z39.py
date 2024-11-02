#Napisać program, który wyznacza liczbę zer jakimi kończy się liczba N!
# Program powinien działać dla N rzędu 10^100


def zeros(n=10**100):

    count = 0
    power_of_5 = 5

    while power_of_5<=n:
        count += n // power_of_5
        power_of_5 *= 5

    return count

N= 10**100
print(zeros(N))
