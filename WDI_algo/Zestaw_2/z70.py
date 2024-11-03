#Napisać funkcję, która dla N-elementowej tablicy T wypełnionej liczbami naturalnym wyznacza długość najdłuższego,
#spójnego podciągu geometrycznego.

def find_geo_seq(T):
    current_len=2
    max_len=2
    q=T[1]/T[0]

    for i in range(2,len(T)):
        if T[i]/T[i-1] ==q:
            current_len+=1
        else:
            q=T[i]/T[i-1]
            current_len=2

        if current_len>max_len:
            max_len=current_len
    return max_len

print(find_geo_seq(T=[1,2,3,4,5,6,7,8,2,4,8,16,32,1,64]))