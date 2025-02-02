from sympy.physics.units import current


class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def display(head):
    cur_node = head
    while cur_node:
        print(cur_node.val, end= " -> ")
        cur_node = cur_node.next
    print("None")

def list_to_ll(l:list):
    head = current = Node(l[0])
    for i in range(len(l)):
        new = Node(l[i])
        current.next = new
        current = new # przepisujemy current na new zeby nastpenym razem moc przejsc do nastepnego wsakznika
    #current.next = head # tworzymy cykl ostatni wezel wskazuje na pierwszy
    return head



def bubble_sort_swap_val(head: Node):
    if head is None or head.next is None:
        return head

    swapped = True # czy cos sie zmienilo
    while swapped:
        swapped = False
        current = head
        while  current is not None and current.next is not None:
            if current.val > current.next.val:
                current.val, current.next.val = current.next.val, current.val
                swapped = True
            current = current.next
        display(head)

    return head

def bubble_sort_swap_nodes(head:Node):
    if head is None or head.next is None:
        return head

    swapped = True
    while swapped:
        swapped = True
        prevNode = head
        current = head

        while current.next is not None:
            ptr = current.next
            if current.val > ptr.val:
                swapped = True

                if current == head: # jestesmy na poczatku
                    current.next = ptr.next # pierwszy wyraz laczymy z trzecim zeby usunac
                    ptr.next = current # zamieniamy kolejnosc wskaznik
                    prevNode = ptr
                    head = prevNode
                else: # jestesmy w srodku
                    current.next = ptr.next
                    ptr.next = current
                    prevNode = ptr
                    head = prevNode
                continue
            prevNode = current
            current = ptr

        display(head)
    return head



head = list_to_ll([4,2,5,1,3])
print("start")
display(head)

print("process")
head = bubble_sort_swap_val(head)
print("result")
display(head)