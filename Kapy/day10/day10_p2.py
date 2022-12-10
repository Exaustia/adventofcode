
cycle = x = 1
screen = CRTrow = ''

def draw():
    global screen
    global CRTrow
    if abs(len(CRTrow)-x) <= 1:
        CRTrow += '#'
    else:
        CRTrow += '.'
    if len(CRTrow) % 40 == 0:
        screen += CRTrow + '\n'
        CRTrow = ''

with open('./Kapy/day10/input.txt', 'r') as f:
    for line in f.readlines():
        instruction = line.strip().split(' ')[-1]
        cycle += 1
        draw()     
        if instruction != 'noop':
            cycle += 1
            draw()
            x += int(instruction)

print(screen)