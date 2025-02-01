# Dana jest kwadratowa tablica T wypełniona liczbami naturalnymi. Proszę napisać funkcję square(T),
# która znajdzie w tablicy największy kwadrat, złożony wyłącznie z elementów, które w zapisie ósemkowym złożone
# są z niepowtarzających się cyfr. Do funkcji należy przekazać tablicę, funkcja powinna
# zwrócić długość boku znalezionego kwadratu. Kwadrat 1 × 1 też jest kwadratem. W przypadku
# nieznalezienia żadnego kwadratu należy zwrócić wartość 0. Dane wejściowe w tablicy mają pozostać
# niezniszczone


def decimal_to_octal(x):
    if x==0:
        return 0
    octal_num = 0
    place=1

    while x>0:
        last_num=x%8
        octal_num+=last_num*place
        x//=8
        place*=10

    return octal_num

def find_unique(n):
    octal_num = decimal_to_octal(n)
    seen = set()

    while octal_num > 0:
        digit = octal_num%10
        if digit in seen:
            return False
        seen.add(digit)
        octal_num//=10

    return True

def is_valid_square(t,x,y,size):
    for i in range(x,x+size):
        for j in range(y,y+size):
            if not find_unique(t[i][j]):
                return False
    return True

def square(t):
    n= len(t)
    max_size = 0

    for size in range(n,0,-1):
        for i in range(n-size +1):
            for j in range(n-size+1):
                if is_valid_square(t, i,j,size):
                    return size
    return 0

T = [
    [12, 8, 15],
    [7, 9, 5],
    [3, 17, 6]
]

print(square(T))
