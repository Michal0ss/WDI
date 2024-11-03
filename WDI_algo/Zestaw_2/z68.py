# Napisać funkcję, która dla N-elementowej tablicy T wypełnionej liczbami naturalnym wyznacza długość najdłuższego,
# spójnego podciągu rosnącego.

def find_sequence(T):
    max_length = 1
    current_length=1

    for i in range(1,len(T)):
        if T[i]>T[i-1]:
            current_length+=1
            if current_length>max_length:
                max_length=current_length
        else:
            current_length=1
    return max_length

print(find_sequence(T=[1,1,7,8,10,11,20,21]))