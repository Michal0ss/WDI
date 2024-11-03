#Napisać funkcję, która dla N-elementowej tablicy T wypełnionej liczbami naturalnym wyznacza długość najdłuższego,
# spójnego podciągu arytmetycznego.


def find_arithmetic_seq(T):
    current_len=2
    max_len=2
    r=T[1]-T[0]

    for i in range(2,len(T)):
        if T[i]-T[i-1]==r:
            current_len+=1
        else:
            r=T[i]-T[i-1]
            current_len=2

        if current_len>max_len:
            max_len=current_len

    return max_len

print(find_arithmetic_seq(T=[3,9]))