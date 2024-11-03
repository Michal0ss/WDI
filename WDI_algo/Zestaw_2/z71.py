#Proszę napisać program, który wypełnia N-elementową tablicę T pseudolosowymi liczbami
#nieparzystymi z zakresu [1..99], a następnie wyznacza i wypisuje różnicę pomiędzy długością najdłuższego
#znajdującego się w niej ciągu arytmetycznego o dodatniej różnicy,
#a długością najdłuższego ciągu arytmetycznego o ujemnej różnicy,
#przy założeniu, że kolejnymi wyrazami ciągu są elementy tablicy o kolejnych indeksach.
#r+ - r-
import random


def longest_arithmetic_subsequence(T, positive_r=True):
    max_length = 1
    current_length = 1
    for i in range(1, len(T)):

        r = T[i] - T[i - 1]

        if (positive_r and r > 0) or (not positive_r and r < 0):
            current_length += 1
        else:
            if current_length>max_length:
                max_length=current_length

            current_length=1 # reset aktualnego ciagu

    if current_length>max_length:
        max_length=current_length

    return max_length


def generate_odd_array(N):
    return [random.choice(range(1, 100, 2)) for _ in range(N)]


def main(N):
    T = generate_odd_array(N)
    print("Tablica T:", T)


    longest_positive = longest_arithmetic_subsequence(T, positive_r=True)
    longest_negative = longest_arithmetic_subsequence(T, positive_r=False)


    difference = longest_positive - longest_negative


    print("Najdłuższy ciąg arytmetyczny o dodatniej różnicy ma długość:", longest_positive)
    print("Najdłuższy ciąg arytmetyczny o ujemnej różnicy ma długość:", longest_negative)
    print("Różnica długości:", difference)


main(10)



