
def isOpenSpace(t):
    x,y = t
    n = x*x + 3*x + 2*x*y + y + y*y
    b = format(n+favNb, 'b')
    return b.count('1') % 2 == 0

def getAround(pos):
    p1 = (pos[0], pos[1]+1)
    p2 = (pos[0], pos[1]-1)
    p3 = (pos[0]+1, pos[1])
    p4 = (pos[0]-1, pos[1])
    return [x for x in [p1, p2, p3, p4] if isOpenSpace(x) and x[0]>=0 and x[1]>=0]

i = 1
maze = {(1,1)}
checked = {(1,1)}
favNb = int(open('./2016/day13/input.txt', 'r').read())
while(True):
    around = set()
    for pos in maze:
        around.update(getAround(pos))
    maze = around.difference(checked)
    if (31,39) in maze:
        print(i)
        break
    checked.update(around)
    i += 1