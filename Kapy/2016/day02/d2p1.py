
pad = {(0,0):'1', (1,0):'2', (2,0):'3',
       (0,1):'4', (1,1):'5', (2,1):'6',
       (0,2):'7', (1,2):'8', (2,2):'9'}
code = ''
pos = list(list(pad.keys())[list(pad.values()).index('5')]) # get the position of "5"

for line in open('./2016/day02/input.txt', 'r').read().splitlines():
    for x in line:
        if x == 'U' and (pos[0], pos[1]-1) in pad.keys():
            pos[1] -= 1
        elif x == 'D' and (pos[0], pos[1]+1) in pad.keys():
            pos[1] += 1
        elif x == 'L' and (pos[0]-1, pos[1]) in pad.keys():
            pos[0] -= 1
        elif x == 'R' and (pos[0]+1, pos[1]) in pad.keys():
            pos[0] += 1
    code += pad[tuple(pos)]
print(code)