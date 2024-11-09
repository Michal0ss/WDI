# Dana jest N-elementowa tablica t wypełniona liczbami naturalnymi. Proszę napisać funkcję,
# która zwraca długość najdłuższego, spójnego podciągu rosnącego dla którego suma jego elementów jest
# równa sumie indeksów tych elementów. Do funkcji należy przekazać tablicę, funkcja powinna zwrócić długość
# znalezionego podciągu lub wartość 0 jeżeli taki podciąg nie istnieje.
def is_rising_and_sum(t):
    s=0
    for i in range(len(t)-1):
        if t[i]>=t[i+1]:
            return False
        s+=t[i]
    s+=t[-1]
    return s


def find_ideal_seq(t):
    n=len(t)
    max_len=0
    for i in range(n):
        for j in range(i,n):
            second_seq=t[i:j+1]

            s = is_rising_and_sum(second_seq)
            if s is not False:
                sum_id = 0
                for k in range(i,j+1):
                    sum_id +=k

                if s==sum_id:
                    if len(second_seq) > max_len:
                       max_len = len(second_seq)

    return max_len if max_len > 0 else 0

t = [1, 1, 1, 3, 15, 21]
print("Długość najdłuższego podciągu:", find_ideal_seq(t))