class Klocek:
    def __init__(self,a,b,next=None):
        self.a=a
        self.b=b
        self.next=next

def get_size(p):
    result = 0
    while p is not None:
        result +=1
        p=p.next
    return result


def mag_mina(p):
    n=get_size(p)
    klocek_list = [None for _ in range(n)]
    iterator=0
    while p is not None:
        klocek_list[iterator] = p
        p=p.next
        klocek_list[iterator].next = None
        iterator+=1

    def mag_mina_rekur(current_setup, klocek_rest):
        nonlocal result, klocek_list
        if current_setup == len(current_setup):
            result = current_setup
            return

        for i in range(len(klocek_rest)):
            if klocek_rest[i]:
                klocek=klocek_list[i]
                if klocek_list[current_setup[-1].b] == klocek.a:
                    mag_mina_rekur(current_setup +klocek,)