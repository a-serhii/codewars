def find_outlier(integers):
    if len([i for i in integers if i % 2 == 0]) == 1:
        return [i for i in integers if i % 2 == 0][0]
    else:
        return [i for i in integers if i % 2 != 0][0]
