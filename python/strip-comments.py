def solution(string, markers):
    if not markers:
        return string
    ready = []
    for str_split in string.split("\n"):
        rez_mark = []
        for mark in markers:
            split_first = str_split.split(mark)[0].strip()
            if len(split_first) < len(str_split):
                split_ready = split_first
            else:
                split_ready = str_split
            rez_mark.append(split_ready)
        ready.append(min(rez_mark))

    return "\n".join(ready)
