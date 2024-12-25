# ====================================================================================================>
# Zadanie 149
# Wyrazy budowane są z liter a..z. Dwa wyrazy ”ważą” tyle samo jeżeli: mają tę samą
# liczbę samogłosek oraz sumy kodów ascii liter z których są zbudowane są identyczne, na przykład ′′ula′′ →
# 117,108,97oraz′′exe′′ →101,120,101.Proszę napisać funkcję wyraz(s1,s2), która sprawdza czy jest możliwe
# zbudowanie wyrazu z podzbioru liter zawartych w s2 ważącego tyle co wyraz s1. Dodatkowo funkcja powinna
# wypisać znaleziony wyraz.
# ====================================================================================================>
# jak sie da wypisz wyraz zwroc True
# jak sie nie da zwroc False

#def ascii_translate(word):
#    alfabet_male = "abcdefghijklmnopqrstuvwxyz"
#    suma = 0
#    for letter in word:
#        if letter in alfabet_male:
#            suma += alfabet_male.index(letter) + 97
#    return suma # np dla exe mamy 101+120+101=322



def word(s1,s2):
    def count_weight(s):
        vowels = set("aeiouy")
        amount_vowel = sum(1 for char in s if char in vowels)
        sum_ascii = sum(ord(char) for char in s)
        return amount_vowel, sum_ascii

    weight_s1 = count_weight(s1) # liczba samoglosek i suma w decimalu

    def find_subseq(new_word, remaining_word):
        if new_word:
            weight_nword = count_weight(new_word)
            if weight_nword == weight_s1:
                print(f"found word: {new_word}")
                return True

        for index, char in enumerate(remaining_word):
            if find_subseq(new_word + char, remaining_word[:index] + remaining_word[index + 1:]):
                return True
            return False

    return find_subseq("",s2)

# Przykładowe użycie
s1 = "ula"
s2 = "exe"
result = word(s1, s2)
print("Czy znaleziono wyraz?", result)

