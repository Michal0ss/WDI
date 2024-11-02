#Liczba dwu-trzy-piątkowa w rozkładzie na czynniki pierwsze nie posiada innych czynników niż 2, 3, 5.
#Jedynka też jest taką liczbą. Proszę napisać program,
#który wylicza ile takich liczb znajduje się w przedziale od 1 do N włącznie.

def count_and_print_two_three_five_numbers(N):
    count = 0
    power_of_2 = 1

    print("Liczby dwu-trzy-piątkowe w przedziale od 1 do", N, "to:")

    # Zagnieżdżone pętle generujące liczby dwu-trzy-piątkowe
    while power_of_2 <= N:
        power_of_3 =power_of_2
        while power_of_3 <= N:
            power_of_5 = power_of_3
            while power_of_5 <= N:
                print(power_of_5)
                count+=1
                power_of_5 *= 5
            power_of_3 *= 3
        power_of_2 *= 2

    print("Liczba dwu-trzy-piątkowych liczb w przedziale od 1 do", N, "wynosi:", count)

# Przykładowe użycie:
N = int(input("Podaj wartość N: "))
count_and_print_two_three_five_numbers(N)
