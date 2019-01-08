def duplicate_count(text):
    text = text.lower()
    uniq_list = list(set(list(text)))
    rez = []
    for i in uniq_list:
        if text.count(i) > 1:
            rez.append(i)
    return len(rez)
