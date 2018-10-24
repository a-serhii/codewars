import re
def capitals(word):
    #your code here
    p = re.compile('[A-Z]')
    rez = []
    search = p.findall(word)
    for i in range(0, len(word)):
        if word[i] in search:
            rez.append(i)
    return rez
callable('fgfdgfdgIUHJOI')
