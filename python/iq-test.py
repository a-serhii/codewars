def iq_test(numbers):
    list_num = numbers.split()
    even = [i for i in list_num if int(i) % 2 == 0]
    odd = [i for i in list_num if int(i) % 2 != 0]
    if len(even) > len(odd):
        for i in list_num:
            if int(i) % 2 != 0:
                return int(list_num.index(i)) + 1
    else:
        for i in list_num:
            if int(i) % 2 == 0:
                return int(list_num.index(i)) + 1
