# Liczby naturalne reprezentowane jak poprzednim zadaniu. Proszę napisać funkcję dodającą
# dwie takie liczby. W wyniku dodawania dwóch liczb powinna powstać nowa lista.

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

def zad184(p,q):
    remain = 0 # reszta z dodwania (liczba dwucyfrowa)
    head = Node(None)
    guard = head
    while p and q:
        sume = p.val+q.val+ remain
        if sume>=10:
            remain = sume//10
            sume %=10
        head.next = Node(sume)
        head = head.next
        p = p.next
        q = q.next
    while p:
        sume = p.val +remain
        if sume>=10:
            remain = sume//10
            sume %=10
        head.next = Node(sume)
        head = head.next
        p = p.next

    while q:
        sume = q.val +remain
        if sume>=10:
            remain = sume//10
            sume %=10
        head.next = Node(sume)
        head = head.next
        q = q.next

    if remain:
        head.next = Node(remain)
    return guard
