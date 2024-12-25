# ====================================================================================================>
# Zadanie 142
# Poprzednie zadanie. Program powinien wypisywać wybrane odważniki.
# ====================================================================================================>
# return [odwaznik1,odwaznik2]

def weight2(t,n,res,p=0):
    if n==0:
        print(res)
        return True
    if p==len[t]:
        return False
    print()

    return weight2(t,n-t[p],res+[t[p]],p+1) or weight2(t,n,res,p+1) or weight2(t,n+t[p], res+[-1*t[p]],p+1)

def zadanie_141(t,choosen_weight):
    return weight2(t,choosen_weight,res=[])