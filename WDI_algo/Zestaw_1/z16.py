#  Proszę napisać program wyznaczający najmniejszą wspólną wielokrotność 3 zadanych liczb naturalnych.
#NWW(a,b)= ∣a⋅b∣ / NWD(a,b)

def nwd(a,b):

    while b!=0:
        temp =b
        b = a%b
        a = temp
    return a

def nww(a,b):
    return abs(a*b) // nwd(a,b)

def trd_nww(a,b,c):
    return nww(nww(a,b), c)

x=int(input("a "))
y=int(input("b "))
z=int(input("c "))
print(f"NWW liczb {x}, {y} i {z} to: {trd_nww(x, y, z)}")