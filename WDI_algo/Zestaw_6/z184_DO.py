#Dana jest niepusta lista reprezentująca liczbę naturalną. Kolejne elementy listy przechowują
#kolejne cyfry. Proszę napisać funkcję zwiększającą taką liczbę o 1.

#Liczby naturalne reprezentowane jak poprzednim zadaniu. Proszę napisać funkcję dodającą
#dwie takie liczby. W wyniku dodawania dwóch liczb powinna powstać nowa lista.


class Node:
    def __init__(self, data,next= None):
        self.data=data #past data point
        self.next=next #pointer to the next Node

def reverse_linked_list(p):
    prev=None
    head=p
    while head is not None:
        next_node=head.next
        head.next=prev
        prev=head
        head = next_node
    return head


def zad184(p,q):
    rem = 0
    head = None
    guard = None

    #sumowanie elementow wspolnych list p i q
    while p and q:
        sum_val = p.data +q.data + rem
        if sum_val>=10:
            rem = sum_val//10
            sum_val%=10
        else:
            rem=0

        if not head:
            head = Node(sum_val)
            guard = head
        else:
            head.next = Node(sum_val)
            head = head.next

        p = p.next
        q=q.next

    # Obsługa dodatkowych elementów w p
    while p:
        sum_val = p.val + rem
        if sum_val >= 10:
            rem = sum_val // 10
            sum_val %= 10
        else:
            rem = 0

        head.next = Node(sum_val)
        head = head.next
        p = p.next


    while q:
        sum_val = q.val + rem
        if sum_val >= 10:
            rem = sum_val // 10
            sum_val %= 10
        else:
            rem = 0

        head.next = Node(sum_val)
        head = head.next
        q = q.next

    # Dodanie ostatniego przeniesienia, jeśli istnieje
    if rem>0:
        head.next = Node(rem)

    return guard
