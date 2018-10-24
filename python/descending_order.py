# https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python

def Descending_Order(num):
    #Bust a move right here
    z = [int(i) for i in str(num)]
    z.sort(reverse=True)
    return int(''.join([str(i) for i in z]))
