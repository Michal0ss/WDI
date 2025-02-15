# Dana jest niepusta lista cykliczna, zbudowana z elementów zawierających pola key i next, której węzły
# przechowują liczby całkowite. Proszę napisać funkcję separate(p) która rozdziela listę cykliczną na dwie
# listy cykliczne. Pierwsza powinna zawierać klucze parzyste dodatnie, druga klucze nieparzyste ujemne,
# pozostałe elementy należy usunąć z pamięci. Do funkcji należy przekazać wskaźniki na listę z danymi.
# Funkcja powinna zwrócić wskaźniki na powstałe listy oraz liczbę usuniętych elementów.

class Node:
    def __init__(self, key, next = None):
        self.key = key
        self.next = next

def seperate(p):

    positive_even_head = positive_even_tail = Node(None)
    negative_odd_head = negative_odd_tail  = Node(None)
    removed_count=0

    # usuwam cykl
    current = p.next
    p.next = None

    while current:
        #odlaczam biezacy wezel
        next_node = current.next
        current.next = None

        # decyduje co zrobic z odlaczonym
        if current.key > 0 and current.key%2==0:
            positive_even_tail.next = current
            positive_even_tail = current
        elif current.key < 0 and current.key%2==1:
            negative_odd_tail.next = current
            positive_even_tail=current
        else:
            removed_count+=1

        current = next_node

    #tworze cykl
    positive_even_tail.next=positive_even_head.next
    negative_odd_head.next=negative_odd_tail.next

    return positive_even_head.next, negative_odd_head.next, removed_count
