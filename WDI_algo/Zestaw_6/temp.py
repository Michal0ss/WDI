class node:
    def __init__(self, data= None):
        self.data=data #past data point
        self.next=None #pointer to the next node

class linked_list:
    # user cannot access this headnote thats a placeholder,
    # to be able to point to the first element in the list
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data) # it will set the data point inside of the node
        cur = self.head # this stores the node we are currently looking at
        while cur.next!=None:   #if next node is set to none we know that its the last element of the list
            cur = cur.next
        cur.next = new_node
