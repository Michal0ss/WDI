#Napisać program wyznaczający na drodze eksperymentu prawdopodobieństwo tego, że w
#grupie N przypadkowo spotkanych osób, co najmniej dwie urodziły się tego samego dnia roku. Wyznaczyć
#wartości prawdopodobieństwa dla N z zakresu 20-40

import random
from multiprocessing.reduction import duplicate


def birthday_simulation(N, trials=10000):

    def has_duplicate_birthdays(group_size):
        birthdays = [random.randint(1,365) for _ in range(group_size)]
        for i in range(group_size):
            for j in range(i+1, group_size):
                if birthdays[i] == birthdays[j]:
                    return True
        return False

    duplicate_count = 0
    for _ in range(trials):
        if has_duplicate_birthdays(N):
            duplicate_count+=1
    return duplicate_count/trials

if __name__ == "__main__":
    print("N\tProbability")
    for N in range(20, 41):
        probability = birthday_simulation(N)
        print(f"{N}\t{probability:.4f}")