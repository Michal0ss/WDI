# ====================================================================================================>
# Zadanie 173
# wypisywanie elementów łańcucha
# ====================================================================================================>

class Node:
    def __init__(self, data=None,next= None):
        self.data=data #past data point
        self.next=next #pointer to the next Node



class Linked_list:
    # user cannot access this headnote thats a placeholder, to be able to point to the first element in the list
    def __init__(self):
        self.head = Node()

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node is not None:
            cur_node =cur_node.next
            elems.append(cur_node.data)
        print(elems)