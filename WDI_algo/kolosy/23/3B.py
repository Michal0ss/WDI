# ====================================================================================================>
# Zadanie 3B, 2024-01-18
# Dana jest liczba odsyłaczowa, której elementy przechowują niepuste napisy składające się z małych
# liter alfabetu angielskiego. Proszę napisać funkcję make_order(p), która porządkuje elementy listy tak,
# aby na jej początku znalazły się napisy, w których kolejne litery są w porządku rosnącym, natomiast
# na końcu listy znalazły się napisy, w których litery są w porządku malejącym. Pomiędzy powstałymi
# grupami elementów należy wstawić elementy zawierające pusty napis. Do funkcji należy przekazać
# wskaźnik do pierwszego elementu listy, funkcja powinna zwrócić wskazanie do uporządkowanej listy.
# Na przykład lista: ala → ola → abel → ula → irys → ewa → sroka → gips
# Po uporządkowaniu może mieć postać: abel → gips → „” → irys → ala → ewa → „” → sroka → ola → ula
# ====================================================================================================>
def make_order(p):
    malejacy, nijaki, rosnacy = Node(""), Node(""), Node(None)
    nijaki.next, rosnacy.next = malejacy, nijaki
    while p:
        next_p = p.next
        idx = 0 if all(p.val[i] < p.val[i + 1] for i in range(len(p.val) - 1)) \
            else 2 if all(p.val[i] > p.val[i + 1] for i in range(len(p.val) - 1)) \
            else 1
        p.next = [rosnacy, nijaki, malejacy][idx].next
        [rosnacy, nijaki, malejacy][idx].next = p
        p = next_p
    return rosnacy.next