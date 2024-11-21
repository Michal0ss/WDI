# Proszę napisać funkcję, która oblicza ile dni dzieli dwie daty. Na przykład daty 19.05.1964
# i 21.06.1970 dzieli 2224 dni. Do funkcji należy przekazać obie daty, funkcja powinna zwrócić liczbę dni
# pomiędzy tymi datami. Daty mogą pochodzić z lat 1900-2100.


def leap_year(y):
    if y%4==0:
        if y%100==0:
            if y%400==0:
                leap=True
            else:
                leap=False
        else:
            leap = True
    else:
        leap = False

    return leap

def find_date_div(T1,T2):
    md = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    md1,md2=md,md
    ytod1 = (T1[2] - 1900) * 365
    ytod2 = (T2[2] - 1900) * 365

    if leap_year(T1[2]):
        md1[1]=29
        ytod1+=1
    if leap_year(T2[1]):
        md2[1]=29
        ytod2 += 1

    if T1[2]>T2[2]:
        mtod1,mtod2=0,0
        for i in range(1, T1[1]+1):
            mtod1+=md1[i]
        for j in range(1, T2[1] + 1):
            mtod2 += md2[j]
        deference= (ytod1+mtod1+T1[0])-(ytod2+mtod2+T2[0])
        return deference






T1=[]
for _ in range(3):
    print("Enter one by one day month a year")
    x=int(input())
    T1.append(x)
print(T1)

T2=[]
for _ in range(3):
    print("Enter one by one day month a year")
    z=int(input())
    T2.append(z)

print(T2)

print(find_date_div(T1,T2))