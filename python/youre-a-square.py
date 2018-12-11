from math import sqrt


def is_square(n):
    try:
        if int(sqrt(n)) ** 2 == n:
            return True
        else:
            return False  # fix me
    except:
        return False
