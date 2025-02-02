from sympy import preview


class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def reverse_linked_list(p):
    prev = None
    head = p
    while head is not None:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node

    return head

