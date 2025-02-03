#Napis nazywamy wielokrotnym, jeżeli powstał przez 𝑛-krotne (𝑛 > 1) powtórzenie innego napisu o
#długości co najmniej 1. Przykłady napisów wielokrotnych: ABCABCABC, AAAA, ABAABA. Dana jest
#tablica T[N] zawierająca napisy. Proszę napisać funkcję multi(T), która zwraca długość najdłuższego
#napisu wielokrotnego występującego w tablicy T lub wartość 0, jeżeli takiego napisu nie ma w tablicy



def multi(t):
    najdluzszy = 0
    for napis in t:
        n = len(napis)

        for dlugosc in range(n//2, 0, -1):

            if n%dlugosc == 0:
                element = napis[:dlugosc]
                liczba_powtorzen = n//dlugosc
                if element*liczba_powtorzen == napis:
                    najdluzszy = max(najdluzszy, dlugosc)
                    break
        return najdluzszy