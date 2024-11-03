#Napisać program, który wczytuje wprowadzany z klawiatury ciąg liczb naturalnych zakończonych zerem stanowiącym wyłącznie znacznik końca danych.
#Program powinien wypisać 10 co do wielkości wartość, jaka wystąpiła w ciągu.
# Można założyć, że w ciągu znajduje się wystarczająca liczba elementów.
def tenth_largest():
    top_ten = [0] * 10
    while True:
        num = int(input("Wprowadź liczbę (zero kończy wprowadzanie): "))
        if num == 0:
            break
        if num > top_ten[0]:
            for i in range(len(top_ten)):
                if num>top_ten[i]:
                    top_ten=top_ten[:i] + [num] + top_ten[i:9]
    if top_ten[0] == 0:
        print("Nie wprowadzono wystarczającej liczby wartości większych od zera.")
    else:
        print("Dziesiąta co do wielkości wartość to:", top_ten[0])


tenth_largest()