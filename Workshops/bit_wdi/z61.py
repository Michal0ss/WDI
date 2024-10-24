

#def sort(n,p):
#    return sorted(str(n)) == sorted(str(p))

#n = input("enter 1")
#p = input("enter 2")
#print(sort(n,p))

def check(a,b):
    t = [0 for _ in range(10)]
    i=0
    while a>0:
        print(t[i])
        i+=1
        t[a%10]+=1
        a//=10
    print()
    while b>0:
        print(t[i])
        i+=1
        t[b%10]-=1
        b//=10
    for i in range(10):
        if t[i]!=0:
            return False
    return True


print(check(121,121))