# ====================================================================================================>
# Zadanie 139
# Liczba dwu-trzy-piątkowa w rozkładzie na czynniki pierwsze nie posiada innych czynników
# niż 2,3,5. Jedynka też jest taką liczbą. Proszę napisać funkcję rekurencyjną, wypisującą liczby znajdujące
# się w przedziale od 1 do N włącznie.
# ====================================================================================================>

def zadanie_139(n):
    def multiply(num, latest_mult):

        if num<n:
            return

        print(num)

        multiply(num*5,5)

        if latest_mult <= 3:
            multiply(num*3,3)

        if latest_mult <=2:
            multiply(num*2,2)

    multiply(1,1)