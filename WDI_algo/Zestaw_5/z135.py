def move(t,w,k,price):
    global mini
    if w == 7:
        mini  = min(mini,price)
        return
    move(t,w+1,k,price+t[w+1][k])

    if k>0:
        move(t,w+1,k-1,price+t[w+1][k-1])
    if k<len(t)-1:
        move(t,w+1,k+1,price+t[w+1][k+1])