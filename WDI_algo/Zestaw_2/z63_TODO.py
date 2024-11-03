# Proszę napisać program obliczający i wypisujący stałą e z rozwinięcia w szereg e = 1/0! +
# 1/1! + 1/2! + 1/3! + ... z dokładnością N cyfr dziesiętnych (N jest rzędu 1000).

#def equation():
#    e=1
#    n=1
#    w=1 # wartosc calego np. 1/2! itd
#    while(w>0):
#        e+=w
#        n+=1
#        w/=n
#    return e

#print(equation())

#def equation1(n):
#    e=[0 for _ in range(n)]
#    w=[0 for _ in range(n)]
#    e[0]=1
#    w[0]=1
#    n=1
#    while(check(w)):
#        p=0
#        for i in range(n-1, -1, -1):
#            s=e[i]+ w[i]+p
#            p=s//10
#            e[i]=s%10
#        n+=1
#
#def check():
#    ...
def check(w):
    # Sprawdzenie, czy jakikolwiek element w `w` jest różny od zera
    for digit in w:
        if digit != 0:
            return True
    return False



def equation1(n):
    # Inicjalizacja tablic przechowujących liczby jako listy cyfr
    e = [0 for _ in range(n)]# Lista na wynik rozwinięcia (przechowująca liczby)
    w=[0 for _ in range(n)]# Lista na kolejne wyrazy szeregu
    e[0] = 1  # Ustawienie początkowej wartości `e` (bo zaczynamy od 1/0!)
    w[0] = 1  # Początkowy wyraz szeregu to 1/1! = 1

    term_denominator = 1  # Mianownik odpowiadający za silnię w każdym kroku (1, 2, 3, ...)

    # Dopóki są niezerowe elementy w `w`, obliczamy kolejne wyrazy szeregu
    while check(w):
        # Dodaj `w` do `e` i aktualizuj `e` poprzez dodawanie cyfrowe z przeniesieniem
        carry = 0
        for i in range(n - 1, -1, -1):
            sum_digits = e[i] + w[i] + carry
            carry = sum_digits // 10
            e[i] = sum_digits % 10

        # Aktualizuj wyraz `w` przez podzielenie przez kolejne wartości silni
        term_denominator += 1
        carry = 0
        for i in range(n):
            current = w[i] + carry * 10
            w[i] = current // term_denominator
            carry = current % term_denominator

    return e


# Przykład użycia:
N = 100  # liczba cyfr, do której chcemy obliczyć e
result = equation1(N)

# Wypisanie wyniku jako ciąg cyfr
print("Stała e z dokładnością do", N, "cyfr dziesiętnych:")
print("".join(map(str, result)))



