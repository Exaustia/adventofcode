
file = [int(line) for line in open('./Kapy/day20/input.txt', 'r').read().split('\n')]
tt = len(file)
mod = tt-1 # really ...
order = [i for i in range(tt)]

for i in range(tt):
    pos = order.index(i)
    elem = file[pos]
    if pos + elem > 0:
        newIndex = (pos+elem)%mod
    else:
        newIndex = (pos+elem)%-mod if (pos+elem)%-mod != 0 else mod
    file.insert(newIndex, file.pop(pos))
    order.insert(newIndex, order.pop(pos))

zero = file.index(0)
print(file[(zero+1000)%tt] + file[(zero+2000)%tt] + file[(zero+3000)%tt])