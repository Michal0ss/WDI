#Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy jej
#cyfry stanowią ciąg rosnący.

#niech n = l naturalna
# 1. n%10=x     123%10=3
# 2. if next_x > x return true
# 3. n//=10

def check(n):
    previous_d=10

    while n>0:
        digit=n%10
        if digit>=previous_d:
            return False
        previous_d = digit
        n//=10
    return True

n = int(input("Podaj liczbę naturalną: "))

if n >= 0:
    if check(n):
        print(f"Cyfry liczby {n} stanowią ciąg rosnący.")
    else:
        print(f"Cyfry liczby {n} nie stanowią ciągu rosnącego.")
else:
    raise ValueError("Liczba musi być naturalna (większa lub równa zeru).")