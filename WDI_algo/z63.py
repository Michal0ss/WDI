# Proszę napisać program obliczający i wypisujący stałą e z rozwinięcia w szereg e = 1/0! +
# 1/1! + 1/2! + 1/3! + ... z dokładnością N cyfr dziesiętnych (N jest rzędu 1000).

#def equation():
#    e=1
#    n=1
#    w=1 # wartosc calego np. 1/2! itd
#    while(w>0):
#        e+=w
#        n+=1
#        w/=n
#    return e

#print(equation())

def equation1(n):
    e=[0 for _ in range(n)]
    w=[0 for _ in range(n)]
    e[0]=1
    w[0]=1
    n=1
    while(check(w)):
        p=0
        for i in range(n-1, -1, -1):
            s=e[i]+ w[i]+p
            p=s//10
            e[i]=s%10
        n+=1

def check():
    ...