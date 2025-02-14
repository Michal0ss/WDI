


def convert_to_bases(num) -> dict:
    results = {}
    digits = "0123456789ABCDEF"  # Lista cyfr i liter dla systemów do 16

    for base in range(2, 17):  # Od systemu binarnego (2) do szesnastkowego (16)
        if base < 10:
            converted1 = 0
            place_value = 1
            n = num
            while n > 0:
                remainder = n % base
                converted1 += remainder * place_value
                place_value *= 10
                n //= base
            results[base] = converted1 if converted1 else 0
        else:
            converted = ""
            n = num
            while n > 0:
                remainder = n % base
                converted = digits[remainder] + converted  # Dodajemy cyfrę na początek
                n //= base
            results[base] = converted if converted else "0"  # Jeśli wynik to 0, przypisujemy "0"

    return results