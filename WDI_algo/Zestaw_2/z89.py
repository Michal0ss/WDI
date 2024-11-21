#Korzystając z funkcji z poprzedniego zadania oraz wiedząc, że 1 stycznia 1900 roku był
#poniedziałek, proszę napisać program obliczający jaki dzień tygodnia przypada na określoną datę

def leap_year(y):
    if y%4==0:
        if y%100==0:
            if y%400==0:
                leap=True
            else:
                leap=False
        else:
            leap = True
    else:
        leap = False

    return leap

def find_date_div(T1, T2):
    md = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    md1, md2 = md[:], md[:]  # Tworzymy kopie listy `md` dla niezależnych modyfikacji
    ytod1 = (T1[2] - 1900) * 365
    ytod2 = (T2[2] - 1900) * 365

    # Uwzględnienie lat przestępnych
    if leap_year(T1[2]):
        md1[1] = 29
        ytod1 += 1
    if leap_year(T2[2]):
        md2[1] = 29
        ytod2 += 1

    mtod1 = sum(md1[:T1[1] - 1]) + T1[0]  # Dni od początku roku dla T1
    mtod2 = sum(md2[:T2[1] - 1]) + T2[0]  # Dni od początku roku dla T2

    deference = abs((ytod1 + mtod1) - (ytod2 + mtod2))  # Używamy różnicy bezwzględnej
    return deference


def dzien_tygodnia(dzien, miesiac, rok):
    # Lista dni tygodnia
    dni_tygodnia = ["poniedziałek", "wtorek", "środa", "czwartek", "piątek", "sobota", "niedziela"]

    # Data bazowa: 1 stycznia 1900 (poniedziałek)
    T1 = [1, 1, 1900]
    T2 = [dzien, miesiac, rok]

    # Liczba dni od 1 stycznia 1900 do T2
    liczba_dni = find_date_div(T1, T2)

    # Oblicz dzień tygodnia
    indeks_dnia = liczba_dni % 7
    return dni_tygodnia[indeks_dnia]

# Przykład użycia
print("Podaj dzień, miesiąc i rok:")
dzien = int(input("Dzień: "))
miesiac = int(input("Miesiąc: "))
rok = int(input("Rok: "))

print(f"Dzień tygodnia dla {dzien}.{miesiac}.{rok} to {dzien_tygodnia(dzien, miesiac, rok)}")