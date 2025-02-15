# Dane jest słowo składające się z małych liter alfabetu angielskiego. Słowo to tniemy na co najmniej
# dwa kawałki tak, aby każdy kawałek zawierał dokładnie jedną samogłoskę (aeiouy). Proszę napisać
# funkcję cutting(s), która zwraca liczbę sposobów pocięcia słowa na kawałki.
# Przykłady:
# print(cutting('student')) # zwróci 2 bo stu-dent, stud-ent
# print(cutting('sesja')) # zwróci 3 bo se-sja, ses-ja, sesj-a
# print(cutting('ocena')) # zwróci 4 bo o-ce-na, o-cen-a, oc-e-na, oc-en-a

def cutting(slowo):
    samogloski = ["a", "e", "i", "o", "u"]

    pozycje = []
    for i in range(len(slowo)):
        if slowo[i] in samogloski:
            pozycje.append(i)

    res = 1
    for i in range(1,len(pozycje)):
        res*=pozycje[i]-pozycje[i-1]

    return res
