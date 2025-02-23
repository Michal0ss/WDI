# Dana jest tablica krotek 𝐿 = [(𝑥1, 𝑥2, 𝑦1, 𝑦2), …] gdzie 𝑥1, 𝑥2, 𝑦1, 𝑦2 oznaczają proste ograniczające
# kwadrat (𝑥1 < 𝑥2, 𝑦1 < 𝑦2). Proszę napisać funkcję thirteen(T), która zwraca wartość logiczną
# True, jeśli w danej tablicy można znaleźć 13 nienachodzących na siebie kwadratów, których suma pól
# jest równa 2024 i False w przeciwnym przypadku

def pole(proste):
    return(proste[1]-proste[0])**2

def nachodza(k1,k2:tuple):
    down=k2[3]<k1[2]
    up=k2[2]>k1[3]
    left=k2[1]<k1[0]
    right=k2[0]>k1[1]
    return not (down or up or left or right)

def thirteen(t):
    n=13
    wymagane=2024

    def rek(idx=0, szukane_pole=wymagane, kwadraty = []):
        if szukane_pole==0 and len(kwadraty)==n:
            return True

        if idx==len(t) or len(kwadraty)>n or wymagane<0:
            return False

        if not any(nachodza(t[idx], kwadrat) for kwadrat in kwadraty): # jesli zaden kwadrat nie nachodzi
            if rek(idx+1,szukane_pole-pole(t[idx]), kwadraty +[t[idx]]):
                return True
        return rek(idx+1, szukane_pole, kwadraty)

    return rek()





