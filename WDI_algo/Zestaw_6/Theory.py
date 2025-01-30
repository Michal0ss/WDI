from sympy.integrals.risch import NonElementaryIntegral


class Node:
    def __init__(self, data=None,next= None):
        self.data=data #past data point
        self.next=next #pointer to the next Node

class linked_list:
    # user cannot access this headnote thats a placeholder, to be able to point to the first element in the list
    def __init__(self):
        self.head = Node(None)

    def append(self, data):
        new_node = Node(data) # it will set the data point inside of the Node
        cur = self.head # this stores the Node we are currently looking at
        while cur.next is not None:   #if next Node is set to none we know that its the last element of the list from the class Node
            cur = cur.next
        cur.next = new_node # when the loop ends we set the next node to new node with the entered data

    def insert_at_beginning(self, data):
        new_node = Node(data) # create a new node
        new_node.next = self.head.next # point the new node to the current node
        self.head.next = new_node # update the heads next to the new node

    def insert_values(self, data_list):
        for data in data_list:
            self.append(data)

    def insert_at(self, index, data):
        if index<0 or index > self.length():
            raise ValueError("invalid error")
        if index == 0:
            self.insert_at_beginning(data)
            return
        count = 0

        cur = self.head
        while cur is not None:
            if count == index:
                new_node = Node(data, cur.next)
                cur.next = new_node
                return
            cur = cur.next
            count+=1


    def length(self):
        cur = self.head
        total = 0
        while cur.next is not None: #iterating through every Node till cur.next is None that means we are in the end of list
            total+=1
            cur = cur.next
        return total

    def display(self):
        elems=[]
        cur_node = self.head
        while cur_node.next is not None:
            cur_node=cur_node.next
            elems.append(cur_node.data)
        print(elems)

    def get(self, index):
        if index >= self.length():
            print("ERROR")
            return None
        cur_idx=0
        cur_node=self.head
        while True:
            cur_node=cur_node.next
            if cur_idx == index: return cur_node.data
            cur_idx+=1


    def erase(self, index):
        if index>=self.length():
            print("Error value")
            return
        cur_idx=0
        cur_node=self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx == index:
                last_node.next=cur_node.next
                return
            cur_idx+=1



ll=linked_list()
my_list = linked_list()


my_list.display()
print(type(my_list))
my_list.append(1)
my_list.append(2)
my_list.append(4)
my_list.append(5)
my_list.append(6)
my_list.insert_at(0,8)
my_list.display()
my_list.erase(3)
my_list.insert_at_beginning(0)
my_list.insert_values([9,9,9,9])

my_list.display()

print(f"index szukany: {my_list.get(2)}")
