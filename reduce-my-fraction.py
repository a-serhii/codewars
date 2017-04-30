def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        our_numbers = []
        our_numbers.append(a)
        our_numbers.append(b)
        a = max(our_numbers)
        b = min(our_numbers)
        while b !=0:
            numbers = []
            a = a % b
            numbers.append(a)
            numbers.append(b)
            a = max(numbers)
            b = min(numbers)
        return a


def reduce(fraction):
    # your code here
    divisor = gcd(fraction[0], fraction[1])
    numerator = int(fraction[0] / divisor)
    denominator = int(fraction[1] / divisor)
    new_fraction = []
    new_fraction.append(numerator)
    new_fraction.append(denominator)
    return new_fraction
