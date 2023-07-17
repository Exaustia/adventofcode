import itertools as iter
import re

def isValid(pos):
    return maze[pos[1]][pos[0]] != '#'

def getAround(pos):
    p1 = (pos[0], pos[1]+1)
    p2 = (pos[0], pos[1]-1)
    p3 = (pos[0]+1, pos[1])
    p4 = (pos[0]-1, pos[1])
    return [x for x in [p1, p2, p3, p4] if isValid(x)]

def pathLength(t):
    i = 1
    s = {posDict[t[0]]} # end of every path
    c = {posDict[t[0]]} # checked
    while(True):
        around = set()
        for pos in s:
            around.update(getAround(pos))
        s = around.difference(c)
        if posDict[t[1]] in s:
            return i
        c.update(around)
        i += 1

maze = open('./2016/day24/input.txt', 'r').read()
goals = re.findall(r'\d+', maze)
maze = maze.split('\n')
posDict = dict()
for y,line in enumerate(maze): # find all numbers positions in the maze
    x = -1
    rgx = True
    while(rgx):
        rgx = re.search(r'(\d)', line[x+1:])
        if rgx:
            x = rgx.span()[0] + x + 1
            posDict.update({rgx.group():(x,y)})

Ls = {}
for g in iter.combinations(goals,2): # get the shortest path between two numbers
    Ls.update({g:pathLength(g)})
    Ls.update({g[::-1]:pathLength(g)})

minL = -1
goals.remove('0')
for g in iter.permutations(goals, len(goals)): # add the length of the paths for every permutation of numbers (every path possible)
    l = Ls['0',g[0]] + Ls[g[0],g[1]] + Ls[g[1],g[2]] + Ls[g[2],g[3]] + Ls[g[3],g[4]] + Ls[g[4],g[5]] + Ls[g[5],g[6]]
    if l < minL or minL == -1:
        minL = l
print(minL)