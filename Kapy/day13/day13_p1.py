
def construct(input):
    tab = []
    i = 0
    while i < len(input):
        x = input[i]
        if x == '[':
            prof = 1
            for j, y in enumerate(input[i+1:]):
                if y == '[':
                    prof += 1
                elif y == ']':
                    prof -= 1
                    if prof == 0: # found the end of block
                        break
            tab.append(construct(input[i+1:i+j+1]))
            i += j + 1
        elif x != ',':
            tab.append(int(x))
        i += 1
    return tab

def compare(x, y): # return 1 if x>y, 0 if x=y, and -1 if x<y
    if type(x) == type(y):
        if type(x) == type(1): # both itegers
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
        if type(x) == type(1): # x integer and y list
            return compare([x], y)
        else:
            return compare(x, [y])

tabRes = []
result = 0
with open('./Kapy/day13/input.txt', 'r') as f:
    for idx, line in enumerate(f.readlines()):
        if idx % 3 == 0:
            p1 = construct(line.strip()[1:-1])
        if (idx-1) % 3 == 0:
            p2 = construct(line.strip()[1:-1])

            for i, x in enumerate(p1):
                if i == len(p2):
                    break
                y = p2[i]
                comp = compare(x, y)
                if comp == 1:
                    break
                elif comp == -1:
                    result += int(idx/3) + 1
                    tabRes.append(int(idx/3) + 1)
                    break

            if comp == 0:
                result += int(idx/3) + 1
                tabRes.append(int(idx/3) + 1)
                
print(tabRes)
print(result)