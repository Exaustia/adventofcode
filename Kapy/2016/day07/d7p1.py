import re

def hasABBA(x):
    return re.search("(\\w)(?!\\1)(\\w)\\2\\1", x) is not None

nb = 0
for ip in open('./2016/day07/input.txt', 'r').read().splitlines():
    inside, outside = [], []
    sequences = re.findall("\\w+", ip)
    for i, seq in enumerate(sequences):
        if i%2 == 0:
            outside.append(hasABBA(seq))
        else:
            inside.append(hasABBA(seq))
    if True in outside and not True in inside:
        nb += 1

print(nb)