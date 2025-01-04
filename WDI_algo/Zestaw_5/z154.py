# ====================================================================================================>
# Zadanie 154
# Tablica T[8][8] zawiera liczby naturalne. Proszę napisać funkcję, która sprawdza czy można
# wybrać z tablicy niepusty podzbiór o zadanej sumie. Warunkiem dodatkowym jest aby żadne dwa wybrane
# elementy nie leżały w tej samej kolumnie ani wierszu. Do funkcji należy przekazać wyłącznie tablicę oraz
# wartość sumy, funkcja powinna zwrócić wartość typu bool.
# ====================================================================================================>

def zad154(T,S):
    def rek(t:list, target_sum:int, current_sum:int, available_row:list[bool], available_col:list[bool])->bool:
        if current_sum>target_sum:
            return False
        if current_sum == target_sum and current_sum != 0:
            return True

        for row in range(8):
            if available_row[row]:
                for col in range(8):
                    if available_col[col]:

                        # zaznaczam wiersz i kolumne po ktorych iterowalem jako uzyte
                        available_row[row]=False
                        available_col[col]=False

                        if rek(t, target_sum, current_sum + t[row][col], available_row, available_col):
                            return True

                        available_row[row] = True
                        available_col[col] = True

        return False

    return rek(t =T, target_sum = S, current_sum= 0, available_row=[True]*8, available_col=[True]*8)

T = [
    [1, 2, 3, 4, 5, 6, 7, 8],
    [8, 7, 6, 5, 4, 3, 2, 1],
    [4, 3, 2, 1, 7, 6, 5, 8],
    [1, 1, 1, 1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2, 2, 2, 2],
    [3, 3, 3, 3, 3, 3, 3, 3],
    [4, 4, 4, 4, 4, 4, 4, 4],
    [5, 5, 5, 5, 5, 5, 5, 5]
]

target_sum = 15

result = zad154(T, target_sum)
print(f"Czy istnieje podzbiór spełniający warunki? {result}")
