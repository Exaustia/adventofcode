from collections import deque as dq

nb = int(open('./2016/day19/input.txt', 'r').read())
moit = int((nb/2))
left = dq([i+1 for i in range(moit+1)])
right = dq([i+moit+2 for i in range(moit)])

even = bool(nb % 2)
while(len(left)>1):
    left.pop() if even else right.popleft()
    right.append(left.popleft())
    left.append(right.popleft())
    even = not even
print(left[0])