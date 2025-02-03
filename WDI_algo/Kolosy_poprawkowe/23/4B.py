#Dane jest słowo składające się z małych liter alfabetu angielskiego. Słowo to tniemy na co najmniej
#dwa kawałki tak, aby każdy kawałek zawierał dokładnie jedną samogłoskę (aeiouy). Proszę napisać
#funkcję cutting(s), która zwraca liczbę sposobów pocięcia słowa na kawałki.

#Przykłady:
#print(cutting('student')) # zwróci 2 bo stu-dent, stud-ent
#print(cutting('sesja')) # zwróci 3 bo se-sja, ses-ja, sesj-a
#print(cutting('ocena')) # zwróci 4 bo o-ce-na, o-cen-a, oc-e-na, oc-en-a

def cutting(slowo):
    samogloski = ["a", "e", "i", "o", "u"]

    # tablica pozycji samoglosek w slowo
    pozycje = []
    for i in range(len(slowo)):
        if slowo[i] in samogloski:
            pozycje.append(i)

    result = 1
    for i in range(1, len(pozycje)):
        result *= pozycje[i] - pozycje[i - 1]

    return result

#def cutting(s):
#    vowels = ["a","e","i","o","u","y"]
#    vowel_positions=[]
#    n=len(s)
#
#    for i in range(n):
#        if s[i] in vowels:
#            vowel_positions.append(i)
#
#    if len(vowel_positions)<2:
#        return 0
#
#    count = 0
#    for i in range(len(vowel_positions)-1):
#        if vowel_positions[i+1] - vowel_positions[i]>1:
#            count += vowel_positions[i+1] - vowel_positions[i]
#        else:
#            count += 1
#
#    return count
#
#print(cutting("student"))
#print(cutting("sesja"))
#print(cutting("ocena"))


