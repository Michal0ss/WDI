
def gold(t):
    primes = [2,3,5,7,11,13,17,19]
    n=len(t)
    def rek(index, balance):
        nonlocal primes, t, n

        if index == n:
            return balance ==0
        adasie=False
        for i in range(-2,3):
            if t[index] -i in primes:
                adasie = adasie or rek(index+1, balance-i)
        return adasie

    return rek(0,0)

