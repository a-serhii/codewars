from functools import reduce
from operator import mul


def persistence(n):
    rez = 0
    while len(str(n)) != 1:
        z = [int(i) for i in str(n)]
        n = reduce(mul, z, 1)
        rez += 1
    return rez
