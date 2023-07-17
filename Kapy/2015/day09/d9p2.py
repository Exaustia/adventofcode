import itertools as iter

dist = {}
input = open('./2015/day09/input.txt', 'r').read().splitlines()
for l in input:
    traj = l.split(' ')
    if traj[0] not in dist:
        dist[traj[0]] = {}
    dist[traj[0]][traj[2]] = int(traj[4])
    if traj[2] not in dist:
        dist[traj[2]] = {}
    dist[traj[2]][traj[0]] = int(traj[4])

routes = []
for route in iter.permutations(dist.keys()):
    d = 0
    for i,_ in enumerate(route):
        if i < len(route)-1:
            d += dist[route[i]][route[i+1]]
    routes.append(d)
print(max(routes))