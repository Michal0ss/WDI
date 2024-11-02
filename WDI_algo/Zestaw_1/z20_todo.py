# poprzednie zad:  Dany jest ciąg określony wzorem: An+1 = (An mod 2) ∗ (3 ∗ An + 1) + (1 − An mod 2) ∗ An/2
# Startując z dowolnej liczby naturalnej > 1 ciąg ten osiąga wartość 1. Proszę napisać program, który znajdzie
# wyraz początkowy z przedziału 2-10000 dla którego wartość 1 jest osiągalna po największej liczbie kroków.

# Dla ciągu z poprzedniego zadania proszę znaleźć najmniejszy wyraz początkowy N, dla
# którego ciąg osiąga wartość 1 dokładnie po N krokach.


def next_term(a):
    if a%2==0:
        return a//2
    else:
        return 3 * a + 1

def sequence_length(start, n):
    length =0
    while length==n:
        start = next_term(start)
        length+=1
    return length


def find_shortest_term():
    ...