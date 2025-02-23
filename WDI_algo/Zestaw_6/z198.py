# Dana jest lista, który zakończona jest cyklem. Napisać funkcję, która zwraca liczbę elementów przed cyklem.

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def first_element_in_cycle(p):
    if not p:
        return p
    slow = p
    fast = p
    while fast.next and fast.next.next:
        slow = slow.next
        fast=fast.next.next
        if slow == fast:
            #gdy sie spotkaja to my wiemy ze od tego elementu do poczatku cyklu
            #jest taka sama odleglosc jak od poczatku listy do poczatku cyklu
            slow2=p
            while True:
                if slow == slow2:
                    return slow.val
                slow = slow.next
                slow2 = slow2.next

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
            slow2=head
            counter = 0
            while True:
                if slow == slow2:
                    return counter
                counter += 1
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