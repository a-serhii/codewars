def get_sum(a, b):
    z = []
    if b > a or b == a:
        for i in range(a, b + 1):
            z.append(i)
    else:
        for i in range(b, a + 1):
            z.append(i)
    return sum(z)
