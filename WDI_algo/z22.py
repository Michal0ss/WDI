# Proszę napisać program wyznaczający wartość liczby e korzystając z zależności: e = 1/0! + 1/1! + 1/2! + 1/3! + ...

def factorial(n):
    result =1
    for i in range(2, n + 1):
        result *= i
    return result


def calculate_e(tolerance=1e-10):
    e = 0  # Przybliżenie liczby e
    n = 0  # Numer wyrazu w szeregu
    term = 1  # Pierwszy wyraz (1 / 0! = 1)

    while term > tolerance:
        e += term
        n += 1
        term = 1 / factorial(n)  # Obliczamy kolejny wyraz szeregu: 1 / n!

    return e


approx_e = calculate_e()
print(f"Przybliżona wartość liczby e: {approx_e}")