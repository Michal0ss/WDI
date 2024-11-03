#Proszę napisać program, który wypełnia N-elementową tablicę T trzycyfrowymi liczbami pseudolosowymi,
#a następnie wyznacza i wypisuje długość najdłuższego podciągu spójnego znajdującego się w tablicy dla którego w tablicy występuje również rewers tego ciągu.
# Na przykład dla tablicy: t=[2, 9,3,1,7 ,11,9,6,7, 7,1,3,9 ,12,15] odpowiedzią jest liczba 4.
import random


def generate_array(N):
    return [random.choice(range(100,999)) for _ in range(N)]

def find_arithmetic_seq(T):
    current_len=2
    max_len=2

    for i in range(1,len(T)):



def reversed_seq(T, subsequence):
    reversed_subsequence = subsequence[::-1]

    for i in range(len(T) - len(reversed_subsequence) +1):
        if T[i]





