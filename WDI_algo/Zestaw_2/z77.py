# Dana jest N-elementowa tablica t jest wypełniona liczbami naturalnymi. Proszę napisać
# funkcję, która zwraca długość najdłuższego spójnego podciągu będącego palindromem złożonym wyłącznie
# z liczb nieparzystych. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić długość znalezionego
# podciągu lub wartość 0 jeżeli taki podciąg nie istnieje.
from sympy.physics.units import second


def is_odd(seq):
    for num in seq:
        if num%2==0:
            return False
    return True

def is_palindrome(t):
    n= len(t)
    for i in range(n//2):
        if t[i]!=t[n-i-1]:
            return False
        return True


def find_palindrome_seq(t):
    n=len(t)
    max_len=0
    for i in range(n):
        for j in range(i, n):
            second_seq= t[i:j+1]
            print(second_seq)
            if is_odd(second_seq):
                if is_palindrome(second_seq):
                    if len(second_seq)>max_len:
                        max_len = len(second_seq)
                        print(max_len)

    return max_len


t = [1, 3, 5, 2 , 1, 3, 4, 1, 5, 3, 6]
print("Długość najdłuższego palindromu z nieparzystych liczb:", find_palindrome_seq(t))

