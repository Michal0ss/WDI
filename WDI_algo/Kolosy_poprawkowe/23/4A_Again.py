# Napis nazywamy wielokrotnym, jeżeli powstał przez 𝑛-krotne (𝑛 > 1) powtórzenie innego napisu o
# długości co najmniej 1. Przykłady napisów wielokrotnych: ABCABCABC, AAAA, ABAABA. Dana jest
# tablica T[N] zawierająca napisy. Proszę napisać funkcję multi(T), która zwraca długość najdłuższego
# napisu wielokrotnego występującego w tablicy T lub wartość 0, jeżeli takiego napisu nie ma w tablicy.

def multi(t):
    najdluzszy_cykl = 0
    for napis in t:
        n=len(napis)

        for dlugosc_cyklu in range(n//2, 0, -1):
            if n % dlugosc_cyklu == 0:
                fragment = napis[:dlugosc_cyklu]
                liczba_powtorzen = n//dlugosc_cyklu
                if fragment*liczba_powtorzen == napis:
                    najdluzszy_cykl  = max(najdluzszy_cykl, dlugosc_cyklu)
                    break

    return najdluzszy_cykl