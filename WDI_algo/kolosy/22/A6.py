# Dana jest niepusta lista cykliczna, zbudowana z elementów zawierających pola val i next, której węzły
# przechowują liczby naturalne. Liczby przechowywane w liście spełniają warunek ”łączności”,
# tzn. dla każdego węzła ostatnia cyfra liczby jest identyczna z pierwszą cyfrą liczby z następnego węzła.
# Proszę napisać funkcję insert(p, n), która wstawia do listy wskazywanej przez wskaźnik p, liczbę n, metodą zastąpienia
# co najmniej dwóch elementów jednym zawierającym wstawioną liczbę. Po wstawieniu nowej liczby nadal
# zachowany powinien być warunek ”łączności”. Funkcja powinna zwrócić o ile skrócona została lista albo
# wartość 0 gdy elementu nie można wstawić do listy.


# Na przykład dla listy zawierającej elementy: 2023 31 17 703 37 707 72 29 902
# po wstawieniu liczby 303 lista może wyglądać następująco: 2023 303 37 707 72 29 902
# Funkcja powinna zwrócić wartość 2.

class Node:
    def __init__(self,val,next=None):
        self.val = val
        self.next = next


def first_digit(x):
    while x>=10:
        x//=10
    return x

def last_digit(x):
    return x%10

def insert(p,n):
    head = p

    while True:
        if last_digit(head.val) == first_digit(n):
            start=head
            current = start.next
            length = 0

            while current != start:
                if first_digit(current.val) == last_digit(n):
                    if length >= 2:
                        start.next = Node(n,current)
                        return length - 1
                current = current.next
                length+=1

            head = head.next
            if head == p:
                break

    return 0
