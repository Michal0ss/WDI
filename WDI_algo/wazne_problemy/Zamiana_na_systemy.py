


def convert_to_bases(num) -> dict:
    results = {}

    for base in range(2,17): # iterujemy po od 2 do 16 bo chce systemy od dwojkowego do szesn
        converted = 0
        place_value = 1
        n = num

        while n > 0:
            remainder = n % base
            converted += remainder * place_value
            place_value*=10
            n //= base

        results[base] = converted # zapisujemy w dict-cie podstawa: skonwertowana liczba

        return results

decimal_number = int(input("Podaj liczbę w systemie dziesiętnym: "))
base_conversions = convert_to_bases(decimal_number)

for base, value in base_conversions.items():
    print(f"Liczba w systemie {base}: {value}")