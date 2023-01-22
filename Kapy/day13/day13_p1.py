
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

result = 0
with open('./Kapy/day13/input.txt', 'r') as f:
    for idx, line in enumerate(f.readlines()):
        if idx % 3 == 0:
            p1 = eval(line.strip())
        if (idx-1) % 3 == 0:
            p2 = eval(line.strip())
            if compare(p1, p2) == -1:
                result += int(idx/3) + 1
                
print(result)