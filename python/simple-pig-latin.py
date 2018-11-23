def pig_it(text):
    p = ["!", ".", ",", "?"]
    z = " ".join([i[1:] + i[0] + "ay" for i in text.split() if i not in p])

    z = z.split()
    text = text.split()

    r = []

    for counter, value in enumerate(text):
        if value not in p:
            r.append(z[counter])
        else:
            r.append(value)
    return " ".join(r)
