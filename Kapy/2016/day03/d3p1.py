
n = 0
for triangle in open('./2016/day03/input.txt', 'r').read().splitlines():
    lengths = [int(x) for x in triangle.split()]
    lengths.sort()
    if lengths[0] + lengths[1] > lengths[2]:
        n += 1
print(n)