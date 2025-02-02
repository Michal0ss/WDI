# Dana jest niepusta lista cykliczna, zbudowana z elementów zawierających pola val i next, której węzły
# przechowują liczby naturalne. Liczby przechowywane w liście spełniają warunek ”łączności”,
# tzn. dla każdego węzła ostatnia cyfra liczby jest identyczna z pierwszą cyfrą liczby z następnego węzła. Proszę napisać
# funkcję insert(p, n), która wstawia do listy wskazywanej przez wskaźnik p, liczbę n, metodą zastąpienia
# co najmniej dwóch elementów jednym zawierającym wstawioną liczbę. Po wstawieniu nowej liczby nadal
# zachowany powinien być warunek ”łączności”. Funkcja powinna zwrócić o ile skrócona została lista albo
# wartość 0 gdy elementu nie można wstawić do listy.
# Na przykład dla listy zawierającej elementy: 2023 31 17 703 37 707 72 29 902
# po wstawieniu liczby 303 lista może wyglądać następująco: 2023 303 37 707 72 29 902
# Funkcja powinna zwrócić wartość 2.

from math import log10

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def insert(p,n):
    head = p
    beginning = head.val//(10**(int(log10(head.val))))
    ending = n%10
    first = None
    last = None
    flag = None
    while flag:
        first_digit = head.val//(10**(int(log10(head.val))))
        if first_digit -- beginning:
            count = 1
            first = head
            head = head.next

            while flag:
                last_digit = head.val % 10
                if last_digit == ending:
                    ...