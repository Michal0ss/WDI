# ====================================================================================================>
# Zadanie 160
# Kwadrat jest opisywany czwórką liczb całkowitych (x1 ,x2 ,y1 ,y2 ), gdzie x1 ,x2 ,y1 ,y2 ozna-
# czają proste ograniczające kwadrat x1 < x2 , y1 < y2 . Dana jest tablica T zawierająca opisy N kwadratów.
# Proszę napisać funkcję, która zwraca wartość logiczną True, jeśli danej tablicy można znaleźć 13 nienacho-
# dzących na siebie kwadratów, których suma pól jest równa 2012 i False w przeciwnym przypadku.
# ====================================================================================================>

def pole(proste) -> int:
    return (proste[1]-proste[0]) ** 2

def nachodza(k1,k2:tuple) -> bool:
    down = k2[3]<k1[2]
    up = k2[2]>k1[3]
    left = k2[1]<k1[0]
    right = k2[0]>k1[1]

    return not (left or right or up or down)

def zad_160(t):
    N= 13
    wymagane_pole = 2012

    def rek(idx=0, szukane_pole = wymagane_pole, kwadraty =[]): # lista kwadratow ktore na siebie nie nachodza

        if len(kwadraty) == N and szukane_pole == 0:
            return True

        if idx == len(t) or len(kwadraty)>N or szukane_pole < 0:
            return False

        if not any(nachodza(t[idx], kwadrat) for kwadrat in kwadraty):
            if rek(idx+1, szukane_pole-pole(t[idx]), kwadraty + [t[idx]]):
                return True

        return rek(idx+1, szukane_pole, kwadraty)


    return rek()

t = [
    (0, 2, 0, 2),   # Pole = 4
    (3, 5, 3, 5),   # Pole = 4
    (6, 8, 6, 8),   # Pole = 4
    (9, 11, 9, 11), # Pole = 4
    (12, 14, 12, 14), # Pole = 4
    # ... dodaj więcej przykładów
]
print(zad_160(t))
