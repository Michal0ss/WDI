# Napisać funkcje sprawdzającą czy dwie liczby naturalne są one zbudowane z takich samych
# cyfr, np. 123 i 321, 1255 i 5125, 11000 i 10001.

def check(a,b):
    t=[0 for _ in range(10)]
    i=0
    while a>0:
        print(t[i])
        i+=1
        t[a%10]+=1
        a//=10
    print()
    while b>0:
        print(t[i])
        i += 1
        t[b%10]-=1
        b//=10
    for i in range(10):
        if t[i]!=0:
            return False
    return True

print(check(a=1114, b=1141))

