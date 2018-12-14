from math import pow


def square_digits(num):
    return int("".join([str(int(pow(int(i), 2))) for i in str(num)]))
