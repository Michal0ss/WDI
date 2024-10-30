#Proszę napisać funkcję, która zwraca wartość True gdy dwie liczby są zbudowane z tych
#samych cyfr (na przykład: 123 i 231, 5749 i 4597) i wartość False w przeciwnym przypadku.

#def is_same(x,y):
#    original_y = y
#    while x>0:
#        digit_x = x%10
#        while y>0:
#            digit_y = y%10
#            if digit_y==digit_x:
#                print("True ")
#            y //= 10
#        x//=10
#
#
#print(is_same(123,321))

def count_digit_occurrences(n, digit):
    count = 0
    while n > 0:
        if n % 10 == digit:
            count += 1
        n //= 10
    return count


def max_digit(num1, num2):
    """Return the highest digit in the given two numbers."""
    max_digit = 0
    for num in [num1, num2]:
        while num > 0:
            max_digit = max(max_digit, num % 10)
            num //= 10
    return max_digit


def have_same_digits(num1, num2):
    """Return True if two numbers are composed of the same digits, otherwise False."""
    max_d = max_digit(num1, num2)
    for digit in range(max_d + 1):
        if count_digit_occurrences(num1, digit) != count_digit_occurrences(num2, digit):
            return False
    return True


# Example usage
print(have_same_digits(123123321123, 321123321321))  # Output: True