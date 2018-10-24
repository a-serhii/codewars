# https://www.codewars.com/kata/sum-of-digits-slash-digital-root/train/python

def digital_root(n): 
    while len(str(n)) != 1: 
        n = sum([int(i) for i in str(n)])
    return n


# recursion
def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int,str(n))))
