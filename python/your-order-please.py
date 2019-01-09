def order(sentence):
    if sentence == "":
        return ""
    else:
        b = sentence.split()
        rez = ["a" for i in b]
        for z in b:
            pos = int([i for i in list(z) if i.isdigit()][0]) - 1
            rez[pos] = z
        return " ".join(rez)
