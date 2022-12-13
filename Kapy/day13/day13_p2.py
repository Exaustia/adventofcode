
def compare(x, y): # return 1 if x>y, 0 if x=y, and -1 if x<y
    if type(x) == type(y):
        if isinstance(x, int): # both itegers
            return -1 if x < y else 1 if x > y else 0
        else: # both list
            for i in range(0, len(x)):
                if i == len(y):
                    return 1
                comp = compare(x[i], y[i])
                if comp != 0:
                    return comp
            return 0 if len(x) == len(y) else -1
    else:
        if isinstance(x, int): # x integer and y list
            return compare([x], y)
        else:
            return compare(x, [y])

packets = [[[2]], [[6]]]
result = 0
with open('./Kapy/day13/input.txt', 'r') as f:
    for idx, line in enumerate(f.readlines()): # sort all packets
        if (idx - 2) % 3 != 0:
            comp = 0
            p = eval(line.strip())
            for i, p in enumerate(packets):
                comp = compare(p, p)
                if comp == 1:
                    packets.insert(i, p)
                    break
            if comp != 1: # higher than every other one
                packets.append(p)

print((packets.index([[2]])+1) * (packets.index([[6]])+1))