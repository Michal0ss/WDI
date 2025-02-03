# Dane są dwie listy cykliczne powstałe przez zapętlenie listy jednokierunkowej posortowanej rosnąco,
# dla każdej listy dany jest wskaźnik wskazujący przypadkowy element w takiej liście.
# Proszę napisać funkcję, która dla dwóch list cyklicznych usuwa z obu list elementy występujące w obu listach.
# Do funkcji należy przekazać wskaźniki na dwie listy, funkcja powinna zwrócić łączną liczbę usuniętych elementów.

class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def remove_same(p:Node, q: Node):
    while p.val < p.next.val:
        p = p.next
    p = p.next
    p_beginning = p.next

    while q.val < q.next.val:
        q = q.next
    q=q.next
    q_beginning = q.next

    result = 0
    while q.next != q_beginning and p.next != p_beginning:
        if p.val == q.val:
            result += 1
            p= p.next
            q=q.next
        elif p.val < q.val: # jesli mniejsze a lista jest posortowana to msuimy przyspieszyc i dojsc do elementu rownego
            p = p.next
        else:
            q = q.next

    if p.next.val == q.next.val:
        result+=1

    return result
