# Napisać program generujący i wypisujący liczby pierwsze mniejsze od N metodą Sita Eratostenesa

#def sieve_of_eratosthenes(N):
#    # Tworzymy tablicę prawdy (True) dla wszystkich liczb od 0 do N-1
#    prime = [True for _ in range(N)]
#    p = 2
#
#    while p ** 2 <= N:
#        # Jeśli prime[p] nie zmieniło się, to jest liczbą pierwszą
#        if prime[p]:
#            # Aktualizujemy wszystkie wielokrotności p jako nie pierwsze
#            for i in range(p ** 2, N, p):
#                prime[i] = False
#        p += 1
#
#    # Zbieramy wszystkie liczby pierwsze
#    prime_numbers = [p for p in range(2, N) if prime[p]]
#    return prime_numbers
#
#
## Główna funkcja
#def main():
#    N = 600  # Możesz zmienić wartość N na dowolną inną
#    prime_numbers = sieve_of_eratosthenes(N)
#    print(f"Liczby pierwsze mniejsze od {N}:")
#    print(prime_numbers)

def sito(N):
    prime = [True for _ in range(N)]
    p =2

    while p**2<=N:
        if prime[p]:
            for i in range(p**2, N, p):
                prime[i]=False
        p+=1

    prime_num = [p for p in range(2, N) if prime[p]]
    return prime_num

# Uruchomienie głównej funkcji
if __name__ == "__main__":
    main()