# ====================================================================================================>
# Zadanie 167
# Dane jest słowo składające się z liter alfabetu angielskiego. Słowo to tniemy na conajmniej
# dwa kawałki, tak aby każdy kawałek zawierał dokładnie jedną samogłoskę. Proszę napisać funkcję, która
# zwraca liczbę sposobów pocięcia słowa na kawałki.
# ====================================================================================================>
# np bbbabbabb zwraca 3 bo kombinacji jest tyle ile wynosi odleglosc idx miedzy nimi czyli w tym przypadku 3 i 6


def zad_167(word):
    vowels = ["a", "e", "i", "o", "u", "y"]

    positions=[]
    for i in range(len(word)):
        if word[i] in vowels:
            positions.append(i)

    if len(positions) < 2: return 0

    res = 1
    for i in range(1, len(positions)):
        res*=positions[i]-positions[i-1]
        #mnożymy poniewaz to sa tak naprawde kombinacje a tak jak napisane wyzej
        #ilosc kombinacji jest rownowazna odleglosci miedzy samogloskami czyli jesli sa rtylko dwie samogloski
        # to bierzemy tylko odleglosci miedzy nimi a jesli 3 to bierzemy odleglosci miedzy 1-2 i 2-3
        return res