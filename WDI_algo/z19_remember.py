# Dany jest ciąg określony wzorem: An+1 = (An mod 2) ∗ (3 ∗ An + 1) + (1 − An mod 2) ∗ An/2
# Startując z dowolnej liczby naturalnej > 1 ciąg ten osiąga wartość 1. Proszę napisać program, który znajdzie
# wyraz początkowy z przedziału 2-10000 dla którego wartość 1 jest osiągalna po największej liczbie kroków.

def next_term(A):
    """Calculate the next term in the sequence."""
    if A % 2 == 0:
        return A // 2
    else:
        return 3 * A + 1


def sequence_length(start):
    """Calculate the length of the sequence for a given starting value."""
    length = 0
    while start != 1:
        start = next_term(start)
        length += 1
    return length


def find_longest_sequence(min_val, max_val):
    """Find the starting value in the given range with the longest sequence length."""
    max_length = 0
    max_start = min_val
    for i in range(min_val, max_val + 1): # for i in range(2, 10001)
        current_length = sequence_length(i)
        if current_length > max_length:
            max_length = current_length
            max_start = i
    return max_start, max_length


# Define the range
min_val = 2
max_val = 10000

# Find the starting value with the longest sequence
start_val, length = find_longest_sequence(min_val, max_val)
print(f"The starting value {start_val} reaches 1 after {length} steps.")


# 6171, 123, 321, 231,231, .. 1
#ilosc tych liczb do 1
# i poczatkowa wartosc czyli w tym przypadku 6171