# https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python

def disemvowel(string):
    vowel = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
    list_words = [i for i in string.split()]
    rezult = []
    for i in string:
        if i not in vowel:
            rezult.append(i)
    return ''.join(rezult)
