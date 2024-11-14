# Napis nazywamy wielokrotnym, jeżeli powstał przez n-krotne (n > 1) powtórzenie innego
# napisu o długości co najmniej 1. Przykłady napisów wielokrotnych: ABCABCABC, AAAA, ABAABA.
# Dana jest tablica T[N] zawierająca napisy. Proszę napisać funkcję multi(T), która zwraca długość najdłuższego
# napisu wielokrotnego występującego w tablicy T lub wartość 0, jeżeli takiego napisu nie ma w tablicy

def multi(s):
    n=len(s)
    for b in range (1,n//2+1):
        flag = True
        if n%b==0:
            for i in range(b):
                for j in range(b, n, b):
                    if s[i]!= s[j+i]:
                        flag=False
                        break
                if not flag:
                    break
            if flag:
                return
    return 0