# ====================================================================================================>
# Zadanie 174
# Zliczanie elementów łańcucha
# ====================================================================================================>
class Node:
    def __init__(self, data=None,next= None):
        self.data=data #past data point
        self.next=next #pointer to the next Node
class LinkedList:
    def __init__(self):
        self.head= Node()

    def count(self):
        cur = self.head
        total = 0
        while cur.next is not None:
            total+=1
            cur = cur.next
        return total