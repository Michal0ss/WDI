# Proszę napisać program wyliczający pierwiastek równania x^x = 2020 metodą stycznych.

from math import sqrt


def f(x:int):
    return x**x-2020

def equation(s):
    for x in range(int(sqrt(2020))):
        print(f(x))



