# ====================================================================================================>
# Zadanie 175
# Proszę zaimplementować zbiór mnogościowy liczb naturalnych korzystając ze struktury
# listy odsyłaczowej.
# • czy element należy do zbioru
# • wstawienie elementu do zbioru
# • usunięcie elementu ze zbioru
# ====================================================================================================>
from sympy.physics.units import current


class Node:
    def __init__(self, data=None,next= None):
        self.data=data #past data point
        self.next=next #pointer to the next Node
class NaturalNumSet:
    def __init__(self):
        self.head= None

    def contains(self,value):
        if value <0:
            return False

        cur=self.head
        while cur is not None:
            if cur.data == value:
                return True
            cur = cur.next
        return False

    def insert(self, value):
        if value<0:
            return False
        if self.contains(value):
            return

        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def remove_by_value(self, value):
        if value<0:
            return False

        cur = self.head
        prev=None
        while cur is not None:
            if cur.data == value:
                if prev is None: # jesli to pierwszy node to usuwamy go
                    self.head = cur.next
                else:
                    prev.next = cur.next
                return
            prev=cur
            cur=cur.next
