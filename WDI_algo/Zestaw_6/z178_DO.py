#Proszę napisać funkcję, która dla podanej listy odsyłaczowej odwraca kolejność jej elementów.
class Node:
    def __init__(self, data,next= None):
        self.data=data #past data point
        self.next=next #pointer to the next Node


def reverse_linked_list(head):
    prev = None
    while head is not None:
        next_node = head.next
        head.next = prev
        prev = head
        head = next_node
    return prev

c=Node(3)
b=Node(2,c)
a=Node(1,b)

reversed_head = reverse_linked_list(a)
while reversed_head:
    print(reversed_head.data)
    reversed_head=reversed_head.next



