
input = open('./2015/day25/input.txt', 'r').read().split()
goal = int(input[-3][:-1]), int(input[-1][:-1])

tot = int(goal[1]*(goal[1]+1)/2)
tot += int((goal[0]-1)*(goal[1]+goal[1]+goal[0]-2)/2)

n = 20151125
for _ in range(tot-1):
    n = (n * 252533) % 33554393

print(n)