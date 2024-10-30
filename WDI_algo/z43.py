#Dla pewnej N-cyfrowej liczby naturalnej obliczono sumę N-tych potęg cyfr tej liczby otrzymując kolejną liczbę N-cyfrową.
#Na przykład dla liczb: 354, 543, 600, ... suma ta wynosi 216. Niestety pierwotna
#liczba zaginęła ale wiadomo, że była to największa z możliwych takich liczb. Proszę napisać program, który
#na podstawie zachowanej sumy wyznaczy pierwotną liczbę

def find_sum(x,n):
    x_len = n
    digit_sum=0
    for i in range(x_len):
        digit = x% 10
        digit_sum += digit**n
        x//=10
    return digit_sum

def length(number):
    count=0
    while number>0:
        number//=10
        count+=1
    return count

def find_original_number_preserved_sum(sum_preserved, length_n):
    """Finds the largest number whose digits' powers sum to the preserved sum."""
    max_number = 0
    # Iterate over all possible 'length_n' digit numbers in reverse order
    for i in range(10 ** (length_n - 1), 10 ** length_n): # TODO ->  SMART WAY!  remember that
        if find_sum(i, length_n) == sum_preserved:
            max_number = i
    return max_number

# Example usage
preserved_sum = 216  # This should be given or input
length_n =length(preserved_sum)
original_number = find_original_number_preserved_sum(preserved_sum, length_n)
print(original_number)  # Output: 354