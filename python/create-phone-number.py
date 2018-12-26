def create_phone_number(a):
    first = "".join([str(i) for i in a[:3]])
    second = "".join([str(i) for i in a[3:6]])
    third = "".join([str(i) for i in a[6:]])
    # returns "(123) 456-7890"
    return f"({first}) {second}-{third}"
