# ====================================================================================================>
# Zadanie 124
# Dany jest zbiór punktów leżących na płaszczyźnie opisany przy pomocy
# struktury dane= [(x1 ,y1 ),(x2 ,y2 ),(x3 ,y3 ),...(xn ,yn )].
# Proszę napisać funkcję, która zwraca wartość True jeżeli zbiorze istnieją 4 punkty
# wyznaczające kwadrat o bokach równoległych do osi układu współrzędnych, a wewnątrz
# tego kwadratu nie ma żadnych innych punktów. Do funkcji należy przekazać strukturę opisującą położenie
# punktów.
# ====================================================================================================>
from WDI_algo.Zestaw_1.z22 import approx_e


#def Zadanie_124(t):
#    n=len(t)
#    coordinates=[]
#    for i in range(n):
#        for j in range(i+1,n):
#            if t[i][1]==t[j][1]:
#                a= abs(t[i][1]-t[j][1])
#                for k in range(i+1,n):
#                    if t[k][0]==t[i][0] or t[k][0]==t[j][0]:
#                        if abs(t[k][0]-t[i][0]) == a or  abs(t[k][0]-t[j][0]) == a:
#                            for l in range(i+2,n):
#                                if t[l][1] == t[k][1] and t[l][0]==-t[k][0]:
#                                    coordinates.append(t[i],t[j],t[k],t[l])
#                                    if len(coordinates)==4:
#                                        return True


from math import inf

def zadanie_124(t):
    # najblizszy punkt od osi wsp
    najbzszy_osi = inf
    for x,y in t:
        odl = max(abs(x), abs(y))
        if odl < najbzszy_osi:
            najbzszy_osi = odl

    if najbzszy_osi == 0:
        return False

    prawa_gora = (najbzszy_osi, najbzszy_osi)
    prawy_dol = (najbzszy_osi, -najbzszy_osi)
    lewa_gora = (-najbzszy_osi,najbzszy_osi)
    lewy_dol = (-najbzszy_osi,-najbzszy_osi)

    return prawa_gora in t and prawy_dol in t and lewa_gora in t and lewy_dol in t