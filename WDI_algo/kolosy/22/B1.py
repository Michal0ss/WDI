# Dana jest tablica T zawierająca ciąg liczb naturalnych. Maksymalny, spójny podciąg rosnący to taki, w
# którym przed pierwszym elementem nie ma elementu mniejszego, a za ostatnim elementem nie ma elementu
# większego. Proszę napisać funkcję sequence(T) która sprawdza czy w tablicy można znaleźć dwa maksymalne,
# spójne podciągi rosnące, każdy o długości większej od 2, takie aby po ich złączeniu stanowiły jeden
# ciąg rosnący. Funkcja powinna zwrócić wartość True albo False
# Przykłady:
# sequence( [2,15,17,13,17,19,23,2,6,4,8,3,5,7,1,3,2] ) zwróci True
# sequence( [2,15,17,13,17,19,23,2,6,4,8,3,5,7,14,3,2] ) zwróci False



def find_subseq(t):
    n=len(t)
    subseqences=[]
    start=0

    while start<n:
        end=start
        while end + 1 < n and t[end]<t[end+1]:
            end+=1

        if (start == 0 or t[start-1]>=t[start]) and (end==n-1 or t[end+1]<=t[end]):
            if end-start+1>2:
                subseqences.append((start,end)) # zapisuje tuple

        start=end+1
    return subseqences

def connect(sub1, sub2, t):
    start1, end1 = sub1
    start2, end2 = sub2

    return t[end1]<t[start2] or t[end2]<t[start1]

def sequence(t):
    subseq = find_subseq(t)

    if len(subseq) < 2:
        return False

    for i in range(len(subseq)):
        for j in range(i+1,len(subseq)):
            if connect(subseq[i],subseq[j],t):
                return True

    return False


print(sequence([2,15,17,13,17,19,23,2,6,4,8,3,5,7,1,3,2]))  # True
print(sequence([2,15,17,13,17,19,23,2,6,4,8,3,5,7,14,3,2]))  # False




