# Dana jest tablica T zawierająca liczby wymierne reprezentowane w postaci ułamków. Ułamki reprezentowane
# są w postaci krotek składających się z licznika i mianownika. Proszę napisać funkcję longest(T), zwracającą
# długość najdłuższego spójnego podciągu, którego elementy stanowią ciąg geometryczny. W przypadku gdy
# w tablicy nie ma ciągu dłuższego niż 2 elementy, funkcja powinna zwrócić wartość 0.
# Komentarz: Można założyć, że tablica wejściowa liczy więcej niż 2 elementy.
# Przykłady:
# print(longest( [(0,2),(1,2),(2,2),(4,2),(4,1),(5,1)] ) # wypisze 4
# print(longest( [(1,2),(-1,2),(1,2),(1,2),(1,3),(1,2)] ) # wypisze 3
# print(longest( [(3,18),(-1,6),(7,42),(-1,6),(5,30),(-1,6)] ) # wypisze 6
# print(longest( [(1,2),(2,3),(3,4),(4,5),(5,6)] ) # wypisze 0

def longest(t):
    n=len(t)
    if n<3:
        return 0
    max_length = 0
    for i in range(n-1):
        a,b = t[i]
        x,y = t[i+1]

        if a ==0:
            continue

        q_licznik = x*b
        q_mianownik = y*a

        length = 2

        for j in range(i+2, n):
            m,n = t[j]
            if m*b*q_mianownik==a*n*q_licznik :
                length+=1
                x,y = m,n
            else:
                break

        max_length = max(max_length, length)

    return max_length if max_length>2 else 0

print(longest([(0,2),(1,2),(2,2),(4,2),(4,1),(5,1)])) # 4
print(longest([(1,2),(-1,2),(1,2),(1,2),(1,3),(1,2)])) # 3
print(longest([(3,18),(-1,6),(7,42),(-1,6),(5,30),(-1,6)])) # 6
print(longest([(1,2),(2,3),(3,4),(4,5),(5,6)])) # 0