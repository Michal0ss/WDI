# ====================================================================================================>
# Zadanie 5C, 2024-02-06
# Dana jest definicja klasy, której obiekty stanowią elementy listy odsyłaczowej:
# class Node:
#  def init(self, val, next=None):
#  self.val = val
#  self.next = next
# Lista zawiera wartości będące liczbami naturalnymi. Proszę napisać funkcję divide(p) (p wskazuje
# na pierwszy element listy), która rozdziela listę na dwie listy. W pierwszej powinny się znaleźć
# liczby, które są wielokrotnością (co najmniej dwukrotnością) kwadratu dowolnej liczby pierwszej, a w
# drugiej pozostałe liczby. Względny porządek w powstałych listach nie powinien ulec zmianie. Funkcja
# powinna zwrócić wskazania do obu list.
# ====================================================================================================>
from math import sqrt

class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def is_prime(x):
    if x<=1:
        return False
    for i in range(2, int(sqrt(x))+1):
        if x%i==0:
            return False
    return True

def odczepic(val):
    for i in range(2, int(sqrt(val))+1):
        if is_prime(i) and val%(i*i)==0:
            return val/(i*i) > 1
    return False


def divide(p):
    q_head = q_tail = Node(0)
    p_head = Node(0,p)

    prev, curr = p_head, p
    while curr:
        if odczepic(curr.val):
            prev.next = curr.next
            q_tail.next=curr
            q_tail=curr
        else:
            prev = curr
        curr=curr.next

    q_tail.next = None
    return p_head.next, q_head.next
