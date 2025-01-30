#Napis nazywamy wielokrotnym, jeżeli powstał przez 𝑛-krotne (𝑛 > 1) powtórzenie innego napisu o
#długości co najmniej 1. Przykłady napisów wielokrotnych: ABCABCABC, AAAA, ABAABA. Dana jest
#tablica T[N] zawierająca napisy. Proszę napisać funkcję multi(T), która zwraca długość najdłuższego
#napisu wielokrotnego występującego w tablicy T lub wartość 0, jeżeli takiego napisu nie ma w tablicy



def is_multiply(s):
    n=len(s)
    for i in range(1, n//2+1):
        if n%i==0:
            if s == s[:i]*(n//i):
                return True
    return False

def multiply(t):
    max_length=0

    for s in t:
        if is_multiply(s):
            max_length = max(max_length, len(s))

    return max_length
