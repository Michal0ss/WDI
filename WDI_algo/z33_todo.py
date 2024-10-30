# Proszę napisać program wczytujący liczbę naturalną i odpowiadający na pytanie, czy jej
# cyfry stanowią ciąg geometryczny.
# ciag jest geo gdy istnieje takie q ze an+1 = an*q

import math


def get_digit(source, index):
    return (source // int(math.pow(10, index))) % 10


def main():
    x = int(input("Enter a natural number: "))

    index = 0
    last = get_digit(x, index)
    index += 1
    result = True

    while result and math.pow(10, index) <= x:
        curr = get_digit(x, index)
        index += 1
        if curr <= last:
            result = False
        last = curr

    if result:
        print("TAK")
    else:
        print("NIE")


if __name__ == "__main__":
    main()