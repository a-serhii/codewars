def countBits(n):
    return sum([int(i) for i in bin(n).split("0b")[-1]])
