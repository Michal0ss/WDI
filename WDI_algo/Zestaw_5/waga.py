def waga(t,n,p=0):
    if n==0: return True
    # if n<0: return False uswuwamy ten warunek w momencie gdy dokladamy ciezarek do kamienia po prawej

    if p==len(t):return False
    return waga(t,n-t[p],p+1) or waga(t,n,p+1) or waga(t,n+t[p],p+1)

#def waga(t,n):
#    n=len(t)
#    for i in range(n-1,-1,-1):
#        if n>=t[i]:
#            n-=t[i]
#            if n==0:
#                return True
#    return False


