# tym razem mozemy nie tyle ze dodawac odwazniki do kamienia zeby wyrownac
# pokazujemy jakie wagi na prawo jakie na lewo

def waga(t,w,p=0,res=[]):

    print('*', end="")

    n=len(t)
    if w==0:
        print(res)
        return
    if p == len(t):
        return
    waga(t,w-t[p],p+1,res+[t[p]])
    waga(t,w,p+1,res)
    waga(t,w+t[p],p+1,res+[-t[p]])

t=[1,3,9,27]
waga(t,23)