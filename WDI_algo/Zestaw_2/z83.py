# Dana jest tablica T zawierająca liczby wymierne reprezentowane w postaci ułamków.
# Ułamki reprezentowane są w postaci krotek składających się z licznika i mianownika.
# Proszę napisać funkcję zwracającą długość najdłuższego spójnego podciągu, którego elementy stanowią ciąg geometryczny.
# W przypadku gdy w tablicy nie ma takiego podciągu dłuższego niż 2 elementy, funkcja powinna zwrócić wartość 0.
# Można założyć, że tablica wejściowa liczy więcej niż 2 elementy.
from sympy.physics.units import current


def nwd(a,b):
    while b!=0:
        a,b=b,a%b
    return a

def simplify(num,den):
    g=nwd(num,den)
    return num // g, den // g

def find_tuple_seq(T):
    n= len(T)
    max_len=0

    for i in range(n-1):
        q=None
        current_len=1

        for j in range(i+1, n):
            num1,den1 = T[j-1]
            num2,den2 = T[j]
            ration_num = num2*den1
            ration_den = num1*den2
            ratio = simplify(ration_num,ration_den)

            if q is None:
                q=ratio
                current_len+=1
            elif q == ratio:
                current_len+=1
            else:
                break

        return max_len if max_len > 2 else 0


print(find_tuple_seq([(1, 2), (2, 4), (4, 8), (8, 16)]))  # 4
print(find_tuple_seq([(1, 3), (2, 6), (3, 9), (5, 15), (10, 30)]))  # 3
print(find_tuple_seq([(1, 2), (3, 4), (5, 6)]))