
n = 0
tripleTriangle = []
for i, triangle in enumerate(open('./2016/day03/input.txt', 'r').read().splitlines()):
    lengths = [int(x) for x in triangle.split()]
    tripleTriangle.append(lengths)
    if i%3 == 2:
        for j in range(3):
            lengths = [tripleTriangle[0][j], tripleTriangle[1][j], tripleTriangle[2][j]]
            lengths.sort()
            if lengths[0] + lengths[1] > lengths[2]:
                n += 1
        tripleTriangle = []
print(n)