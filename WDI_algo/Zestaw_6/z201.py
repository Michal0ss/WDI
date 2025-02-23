# Proszę napisać funkcję scalającą dwie posortowane listy w jedną posortowaną listę. Do
# funkcji należy przekazać wskazania na pierwsze elementy obu list, funkcja powinna zwrócić wskazanie do
# scalonej listy. - funkcja iteracyjna, - funkcja rekurencyjna.
from sympy.physics.units import current


def scal_sorted(p,q):
    current_p = p
    previous = None
    while p is not None:
        if q is not None and q.val <current_p.val:
            next_q = q.next
            if previous is None:
                q.next = p
                p = q
            else:
                previous.next=q
                q.next = current_p
            previous = q
            q = next_q
        else:
            previous = current_p
            current_p = current_p.next
    previous.next = q
    return p

