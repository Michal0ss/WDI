# ====================================================================================================>
# Zadanie 141
# Poprzednie zadanie, ale odważniki można umieszczać na obu szalkach.
# ====================================================================================================>
# return bool


def weight2(t,n,res=[],p=0):
    if n==0:
        return True
    if p==len[t]:
        return False

    return weight2(t,n-t[p],res+[t[p]],p+1) or weight2(t,n,res,p+1) or weight2(t,n+t[p], res+[-1*t[p]],p+1)

def zadanie_141(t,choosen_weight):
    return weight2(t,choosen_weight)