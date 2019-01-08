def duplicate_encode(word):
    word = word.lower()
    list_word = list(word)
    rez = []
    for i in list_word:
        if word.count(i) > 1:
            rez.append(")")
        else:
            rez.append("(")
    return "".join(rez)
