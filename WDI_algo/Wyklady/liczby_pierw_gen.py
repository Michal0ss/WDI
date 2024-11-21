def primes():
    lp=[2]
    p=2
    yield p
    while True:
        p+=1
        for d in lp:
            if p%d==0: break
        else:
            lp.append(p)
            yield p

for p in primes():
    print(p)