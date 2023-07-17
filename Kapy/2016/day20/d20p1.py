
def union(a,b):
    if a[0] >= b[0] and a[0] <= b[1]: # ex : a = (2,5) an b = (1,3) : 2 is inbetween 1 and 3
        if a[1] > b[1]:
            return [(b[0], a[1])]
    if a[1] <= b[1] and a[1] >= b[0]: # ex : a = (2,5) an b = (4,6) : 5 is inbetween 4 and 6
        if a[0] < b[0]:
            return [(a[0], b[1])]
    if a[0] <= b[0] and a[1] >= b[1]:
        return [a]
    if a[0] >= b[0] and a[1] <= b[1]:
        return [b]
    return [a,b]

ips = []
for r in open('./2016/day20/input.txt', 'r').readlines():
    i = r.find('-')
    s_e = int(r[:i]), int(r[i+1:]) # s_e = start, end
    ranges = set()
    merges = set()
    for rng in ips:
        u = union(s_e, rng)
        if len(u) == 1:
            merges.add(u[0])
        else:
            ranges.add(rng)

    if len(ranges) == len(ips):
        ranges.add(s_e)

    ips = list(ranges)
    if len(merges) > 1:
        ips.append(union(merges.pop(),merges.pop())[0])
    elif len(merges) > 0:
        ips.append(merges.pop())

ips.sort()
for i in range(len(ips)):
    if ips[i+1][0] > ips[i][1] + 1:
        print(ips[i][1] + 1)
        break