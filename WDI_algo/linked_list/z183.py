# Dana jest niepusta lista reprezentująca liczbę naturalną. Kolejne elementy listy przechowują
# kolejne cyfry. Proszę napisać funkcję zwiększającą taką liczbę o 1

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def reverse_linked_list(p):
    prev = None
    head = p
    while head:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node
    return head

def zad184(p):
    remain = 0 # pierwsza cyfra dwucyfrowej liczby z sumy dodawnaia
    head = Node(None)
    guard = head
    if p:
        p.val+=1 # dodajemy do pierwszego elementu poniewaz odwracamy liste
    while p:
        sume = p.val + remain
        if sume>=10:
            remain = sume//10
            sume %=10
        head.next = Node(sume) # tworzymy nowy wezel z wartoscia sume
        head = head.next # przesuwamy wskaznik head na nowy wezel
        p = p.next # przechodzimy do nastepnego elementu W ORYGINALNEJ LISCIE
    return guard.next
