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
def twins():
    g = primes()
    w1 = next(g)
    while True:
        w2 = next(g)
        if w2 - w1 == 2:
            yield w1,w2
            w1 = w2


for a,b in twins():
    print(a,b)
