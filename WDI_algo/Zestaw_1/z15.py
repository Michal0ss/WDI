# Proszę napisać program wyznaczający największy wspólny dzielnik 3 zadanych liczb naturalnych



def nwd(a,b):

    while b!=0:
        temp =b
        b = a%b
        a = temp
    return a

def trd_nwd(a,b,c):
    return nwd(nwd(a,b), c)


x=int(input("a "))
y=int(input("b "))
z=int(input("c "))
print(trd_nwd(x,y,z))