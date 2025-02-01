# Dana jest tablica T zawierająca liczby naturalne. W tablicy na kolejnych pozycjach ukryto pewien ciąg liczb
# o długości co najmniej 3 elementów. Aby ułatwić odnalezienie tego ciągu, zaraz za nim umieszczono ten sam
# ciąg ale każdy z jego elementów pomnożono przez pewną liczbę. Proszę napisać funkcję sequence(T) która odnajdzie ukryty ciąg.
# Funkcja powinna zwrócić indeksy pierwszego i ostatniego elementu ukrytego ciągu.
# Przykłady:
# sequence( [2,5,7,3,2,3,5,7,6,9,15,21,17,19,23,2,6,4,8,3,5,7,1,3,2] ) zwróci 4,7


def find_subseq(t):
    n= len(t)
    for i in range(n-2):
        for length in range(3, (n-i)//2+1):
            first_seq = t[i:i+length]
            second_seq = t[i+length:i+2*length]

            if len(second_seq) != length:
                continue

            q = second_seq[0]/first_seq[0] if first_seq[0] != 0 else None

            if q:
                is_valid = True
                for j in range(length):
                    if second_seq[j] != first_seq[j] * q:
                        is_valid =False
                        break
                if is_valid:
                    return i, i+ length -1

    return None

T = [2, 5, 7, 3, 2, 3, 5, 7, 6, 9, 15, 21, 17, 19, 23, 2, 6, 4, 8, 3, 5, 7, 1, 3, 2]
print(find_subseq(T))  # Powinno zwrócić (4, 7)
