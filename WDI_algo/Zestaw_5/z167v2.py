# to samo tylko rekurencja

# ====================================================================================================>
# Zadanie 167
# Dane jest słowo składające się z liter alfabetu angielskiego. Słowo to tniemy na conajmniej
# dwa kawałki, tak aby każdy kawałek zawierał dokładnie jedną samogłoskę. Proszę napisać funkcję, która
# zwraca liczbę sposobów pocięcia słowa na kawałki.
# ====================================================================================================>
def multiply_distance(positions):
    if len(positions)<2: return 0
    return (positions[1] - positions[0])*multiply_distance(positions[1:])

def rek(word, position=[], idx=0):
    vowels = ["a", "e", "i", "o", "u", "y"]
    if idx==len(word):
        return multiply_distance(position) if len(position) >= 2 else 0

    if word[idx] in vowels:
        print(position)
        return rek(word, position + [idx], idx+1)+rek(word, position, idx+1)
    else:
        print(position)
        return rek(word,position, idx+1)

def count_ways_to_split(word):
    return rek(word)

word = "bbbabbabb"
result = count_ways_to_split(word)
print(result)
