
tot = 0
for dim in open('./2015/day02/input.txt', 'r').read().split():
    tDim = [int(x) for x in dim.split('x')]
    tDim.sort()
    tot += 2*tDim[0]*tDim[1] + 2*tDim[1]*tDim[2] + 2*tDim[0]*tDim[2] + tDim[0]*tDim[1]

print(tot)
