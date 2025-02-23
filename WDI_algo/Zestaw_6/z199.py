# Dana jest lista, który zakończona jest cyklem. Napisać funkcję, która zwraca wskaźnik do
# ostatniego elementu przed cyklem

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next


def amount_elements_before_cycle(head):
    if not head:
        return head
    slow = head
    fast = head
    while fast.next and fast.next.next is not None:
        slow = slow.next
        fast=fast.next.next
        if slow == fast:
            #gdy sie spotkaja to my wiemy ze od tego elementu do poczatku cyklu
            #jest taka sama odleglosc jak od poczatku listy do poczatku cyklu
            slow2=head # slow2 bedzie szedl z poczatku naszej listy az spotka sie na poczatku cyklu
            prev = head # poprzedni zaczynamy od zera
            slow2 = slow2.next  # zwiekszamy po kolei slow1 i slow2
            slow = slow.next

            while True:
                if slow == slow2: # gdy sa rowne zwracamy poprzedni wskaznik
                    return prev
                prev = slow2 # przypisujemy do prev wartoscs przed przesunieciem o jeden
                slow = slow.next
                slow2 = slow2.next


g = Node(7)
f = Node(6,g)
e = Node(5,f)
d = Node(4,e)
c = Node(3,d)
b = Node(2,c)
a = Node(1,b)

g.next = c
print(amount_elements_before_cycle(a))