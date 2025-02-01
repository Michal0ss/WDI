# Dana jest szachownica o wymiarach N ×N. Na szachownicy umieszczono pewną liczbę skoczków
# szachowych. Pole jest bezpieczne, jeżeli nie jest zajmowane przez skoczka i nie jest szachowane przez
# żadnego skoczka. Położenie skoczków na szachownicy opisuje tablica ze współrzędnymi skoczków.
# Usuwamy jednego skoczka z szachownicy, aby odzyskać bezpieczne pola. Proszę napisać funkcję
# usun(T, N), która zwraca maksymalną liczbę pól, które mogą stać się bezpieczne po usunięciu jednego
# skoczka. Można założyć poprawność danych wejściowych.
# Na przykład dla tablic:
# T = [(1, 1), (2, 3), (4, 1), (4, 5)] funkcja powinna zwrócić wartość 7 - usuwamy skoczka (2, 3)
# T = [(1, 0), (2, 3), (4, 1), (4, 5)] funkcja powinna zwrócić wartość 9 - usuwamy skoczka (2, 3)
def attacked_square(t,coordinates:tuple, n:int)-> set:

    x,y = coordinates
    moves = [
        (x + 2, y + 1), (x + 2, y - 1), (x - 2, y + 1), (x - 2, y - 1),
        (x + 1, y + 2), (x + 1, y - 2), (x - 1, y + 2), (x - 1, y - 2)
    ]
    return {(a,b) for a,b in moves if 0<=a<n and 0<b<n}

def delete(t, n):
    max_safe_fields = 0

    total_attacked_fields=set()
    for knight in t:
        total_attacked_fields.update(attacked_square(t, knight, n))
