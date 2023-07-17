
pad = {                      (2,0):'1',
                  (1,1):'2', (2,1):'3', (3,1):'4',
       (0,2):'5', (1,2):'6', (2,2):'7', (3,2):'8', (4,2):'9',
                  (1,3):'A', (2,3):'B', (3,3):'C', 
                             (2,4):'D'}
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