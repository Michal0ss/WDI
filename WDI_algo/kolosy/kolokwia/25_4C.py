class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def fix(p):
    head = p
    prev = None
    prev_start=None
    end=None
    start=None
    while head:
        prev = head
        head = head.next
        if head and head.val<prev.val:
            start=head
            prev_start=prev
        if prev_start and head and head.val>prev_start:
            prev_start=None
            end = prev
            prev_start.next = head
    head = p
    prev=None
    while head:
        if not prev and head.val>end.val:
            end.next=head
            p=start
        prev = head
        head = head.next
        if prev.val<start.val and end.val<head.val:
            prev.next=start
            end.next = head

    print(start.val,end.val)
    return p



