# Proszę napisać program wczytujący trzy liczby naturalne a, b, n i wypisujący rozwinięcie
# dziesiętne ułamka a/b z dokładnością do n miejsc po kropce dziesiętnej. (n jest rzędu 100)

def divide(a,b,n=100):

    int_part = a//b
    print(int_part, end=".")

    w = a % b
    for _ in range(n):
        w *= 10
        digit = w // b
        print(digit, end="")
        w %= b
    print()




try:
    a = int(input("Podaj licznik (a): "))
    b = int(input("Podaj mianownik (b): "))
    n = int(input("Podaj liczbę miejsc po kropce dziesiętnej (n): "))

    divide(a, b, n)
except ValueError as e:
    print(e)
except Exception as e:
    print(f"An unexpected error occurred: {e}")