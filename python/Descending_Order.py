def Descending_Order(num):
    num = list(str(num))
    new_list = []
    for i in num:
        new_list.append(int(i))
    new_list = sorted(new_list)
    new_list.sort(reverse = True)
    rez = ''
    for i in new_list:
        rez += str(i)
    return int(rez)

