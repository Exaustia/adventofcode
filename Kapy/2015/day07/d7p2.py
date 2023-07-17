
def getVal(x):
    if x == 'b':
        return 3176
    elif x.isdigit():
        return int(x)
    else:
        if x in wires:
            return wires[x]
        else:
            for l in input:
                instr = l.split(' ')
                if instr[-1] == x:
                    if instr[1] == '->':
                        val = getVal(instr[0])
                        wires[x] = val
                        return val
                    elif instr[0] == 'NOT':
                        val = (65536 + ~getVal(instr[1])) % 65536
                        wires[x] = val
                        return val
                    elif instr[1] == 'LSHIFT':
                        val = getVal(instr[0]) << getVal(instr[2])
                        wires[x] = val
                        return val
                    elif instr[1] == 'RSHIFT':
                        val = getVal(instr[0]) >> getVal(instr[2])
                        wires[x] = val
                        return val
                    elif instr[1] == 'AND':
                        val = getVal(instr[0]) & getVal(instr[2])
                        wires[x] = val
                        return val
                    elif instr[1] == 'OR':
                        val = getVal(instr[0]) | getVal(instr[2])
                        wires[x] = val
                        return val

wires = {}
input = open('./2015/day07/input.txt', 'r').read().splitlines()
    
print(getVal('a'))