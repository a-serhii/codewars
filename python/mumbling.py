def accum(s):
    rez = []
    x = 1
    for i in s:
        if x != 1:
            rez.append(i.upper() + (i * (x - 1)).lower())
        else:
            rez.append(i.upper())
        rez.append("-")
        x += 1

    return "".join(rez)[:-1]
