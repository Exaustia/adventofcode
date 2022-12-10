
cycle = x = 1
result = 0

def checkCycle(cycle, x):
    if (cycle - 20) % 40 == 0:
        return cycle * x
    return 0
    
with open('./Kapy/day10/input.txt', 'r') as f:
    for line in f.readlines():
        instruction = line.strip().split(' ')[-1]
        cycle += 1
        result += checkCycle(cycle, x)
        if instruction != 'noop':
            cycle += 1
            x += int(instruction)
            result += checkCycle(cycle, x)

print(result)