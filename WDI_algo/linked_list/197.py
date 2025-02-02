# Dana jest lista, który zakończona jest cyklem. Napisać funkcję, która zwraca liczbę elementów w cyklu.

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def zad197(p):
    if not p:
        return p
    slow = p
    fast = p
    while slow.next and fast.next and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            counter = 1
            while slow.next:
                slow = slow.next
                counter+=1
                if slow==fast:
                    return counter
    return 0
  