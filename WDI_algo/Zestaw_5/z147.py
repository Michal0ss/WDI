# ====================================================================================================>
# Zadanie 147
# Problem wież w Hanoi (treść oczywista)
# ====================================================================================================>

def hanoi(n: int, a: list,  b: list, c: list):
    if n>0:
        hanoi(n-1,a, c, b)
        c.insert(0, a.pop(0))
        print(a,b,c)
        hanoi(n-1, b, a, c)
# Liczba krążków
n = 3

# Początkowe wieże
a = [1, 2, 3]  # Wieża początkowa (krążki ułożone od największego na dole do najmniejszego na górze)
b = []         # Wieża pomocnicza (pusta na początku)
c = []         # Wieża docelowa (pusta na początku)

# Wywołanie funkcji
hanoi(n, a, b, c)

# Po wykonaniu funkcji, wieża docelowa 'c' powinna zawierać wszystkie krążki w odpowiedniej kolejności
print("Wieża A:", a)
print("Wieża B:", b)
print("Wieża C:", c)
