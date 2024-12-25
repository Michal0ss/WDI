def count_weight(s):
    vowels = set("aeiouy")
    amount_vowel = sum(1 for char in s if char in vowels)
    sum_ascii = sum(ord(char) for char in s)
    return amount_vowel, sum_ascii

def combinations(letters, k):
    if k == 0:
        yield ""
        return
    if len(letters) < k:
        return

    for comb in combinations(letters[1:], k - 1):
        yield letters[0] + comb

    yield from combinations(letters[1:], k)

def find_w(s1, s2):
    vowels = set("aeiouy")
    vowels_s2 = []
    consonants_s2 = []

    for char in s2:
        if char in vowels:
            vowels_s2.append(char)
        else:
            consonants_s2.append(char)

    # Zmienione: obliczamy wagę s1 raz, zamiast wielokrotnie
    num_vowels_s1, sum_ascii_s1 = count_weight(s1)  # Zmienione

    # Generujemy kombinacje samogłoskowe z s2 o tej samej liczbie samogłosków co w s1
    for vowel_writing in combinations(vowels_s2, num_vowels_s1):
        required = sum_ascii_s1 - count_weight(vowel_writing)[1]  # Zmienione: używamy sumy ASCII z s1

        for k in range(len(consonants_s2) + 1):
            for consonants_writing in combinations(consonants_s2, k):
                if count_weight(consonants_writing)[1] == required:
                    print(consonants_writing + vowel_writing)
                    return True

    return False

s1 = "ula"
s2 = "exeyhad"
result = find_w(s1, s2)
print("Czy znaleziono wyraz?", result)
