def spin_words(sentence):
    return " ".join(
        [(lambda i: i if len(i) < 5 else i[::-1])(i) for i in sentence.split()]
    )
