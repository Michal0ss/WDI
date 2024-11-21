def fib():
    a,b=1,1
    while True:
        yield a
        a,b = b, a+b

sum=0
for w in fib():
    print(w)
    sum+=w
    if sum>10000:
        break