# Dana jest definicja klasy, której obiekty stanowią elementy listy odsyłaczowej.
# class Node:
#  def init(self, val, next=None):
#  self.val = val
#  self.next = next
# Lista zawierała wartości stanowiące kolejne wyrazy ciągu arytmetycznego. Z wnętrza listy usunięto
# pewną liczbę elementów. Proszę napisać funkcję repair(p), (p wskazuje na pierwszy element listy)
# która uzupełnia listę jak najmniejszą liczbą elementów tak, aby ponownie zawierała kolejne wyrazu
# ciągu arytmetycznego. Funkcja powinna zwrócić liczbę wstawionych elementów.
# Komentarz: Można założyć, że lista wejściowa liczy więcej niż 2 elementy

# [2, 4, 6, 8, 10, 12, 14]
# [2, 6, 10, 12, 14]

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def nwd(a,b):
    while b!=0:
        a,b=b,a%b
    return a


def arithmetic_diff(p):
    value_nwd = 1
    r = p.next.val - p.val

    while p.next:
        value_nwd = nwd(r, (p.next.val - p.val))
        p = p.next
    return value_nwd


def repair(p):
    step = arithmetic_diff(p)

    inserted_count = 0
    while p.next:
        if p.val + step != p.next.val:
            p.next = Node(p.val+step, p.next)
            inserted_count+=1
        p = p.next

    return inserted_count



