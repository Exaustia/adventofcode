import re

def reverse(x):
    return x[1]+x[0]+x[1]

def getABAs(txt):
    matchs = []
    while True:
        s = re.search("(\\w)(?!\\1)(\\w)\\1", txt)
        if s is not None:
            matchs.append(s.group())
            txt = txt[s.span()[0]+1:]
            continue
        return matchs

nb = 0
for ip in open('./2016/day07/input.txt', 'r').read().splitlines():
    outside, inside = [], []
    sequences = re.findall("\\w+", ip)
    for i, seq in enumerate(sequences):
        for aba in getABAs(seq):
            if i%2 == 0:
                outside.append(aba)
            else:
                inside.append(aba)
    for aba in outside:
        if reverse(aba) in inside:
            nb += 1
            break
print(nb)