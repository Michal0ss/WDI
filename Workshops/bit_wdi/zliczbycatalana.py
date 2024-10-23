i=0
c=1
n=-1
p=[]
np=[]
while c < 1_000_000:
    i+=1
    n+=1
    c=((4*n+2)/(n+2))*c
    print(f"{i}: {c}")
    if c%2 == 0:
        p.append(c)
    else:
        np.append(c)
print(f"ilosc parzystych {len(p)}\n")
print(f"ilosc nieparzystych {len(np)}\n")
print(f"parzyte: {p}, nieparzyste: {np}")

