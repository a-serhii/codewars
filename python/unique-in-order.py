def unique_in_order(iterable):
    try:
        list_it = list(iterable)
        rez = []
        rez.append(list_it[0])
        for i in list_it:
            if rez[-1] != i:
                rez.append(i)
        return rez
    except IndexError:
        return []
