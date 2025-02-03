class Node:
    def __init__(self, val=None, next = None):
        self.val = val
        self.next = next

def split_y_list(A,B):
    result = 0
    current_a = A
    while current_a is not None:
        current_b = B
        while current_b is not None:
            if current_b.val == current_a.val:
                support = current_a.next
                while support is not None:
                    current_a.next = Node(support.val)
                    current_b.next = Node(support.val)

                    current_b = current_b.next
                    current_a = current_a.next
                    support = support.next
                    result += 1
                return result

            current_b = current_b.next
        current_a = current_a.next
    return result