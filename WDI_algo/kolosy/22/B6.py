# Dana jest niepusta lista cykliczna, zbudowana z elementów zawierających pola key i next, której węzły
# przechowują liczby całkowite. Proszę napisać funkcję separate(p) która rozdziela listę cykliczną na dwie
# listy cykliczne. Pierwsza powinna zawierać klucze parzyste dodatnie, druga klucze nieparzyste ujemne,
# pozostałe elementy należy usunąć z pamięci. Do funkcji należy przekazać wskaźniki na listę z danymi.
# Funkcja powinna zwrócić wskaźniki na powstałe listy oraz liczbę usuniętych elementów.



class Node:
    def __init__(self, val, next = None):
        self.val = val
        self.next = next

def separate(p):
    temp = p.next  # usuwamy cykl usuwajac jeden wsskaznik
    p.next = None
    p = temp

    #głowy od parzystych i nieparzystych
    head_even = last_even = None
    head_odd = last_odd =  None

    removed = 0


    while p is not None:
        p_next = p.next
        p.next = None

        # nieparzyste ujemne
        if p.val < 0 and p.val % 2 == 1:
            if head_odd is None:
                head_odd = last_odd = p
            else:
                last_odd.next = p
                last_odd = last_odd.next

        elif p.val > 0 and p.val % 2 == 0:
            if head_even is None:
                head_even = last_even = p
            else:
                last_even.next = p
                last_even = last_even.next
        else:
            removed += 1

        p = p_next

    if last_even is not None:
        last_even.next = head_even

    if last_odd is not None:
        last_odd.next = head_odd

    return head_even, head_odd, removed
