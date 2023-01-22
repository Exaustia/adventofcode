
volcano = {}

for line in [l.split(' ') for l in open('./Kapy/day16/inputTest.txt', 'r').read().split('\n')]:
    flow = int(line[4].split('=')[1][:-1])
    valves = [x[:2] for x in line[9:]]
    volcano[line[1]] = {'flow' : flow, 'status' : 'closed', 'leadTo' : valves, 'distances' : {}}

# to do : calculate every distances of valve from every valve (including itself)
volcano['AA']['distances'] = [('AA',0), ('DD',1), ('II',1), ('BB',1), ('CC',2), ('JJ',2), ('EE',2)] # etc

def calculGain(tupleDist):
    valve = tupleDist[0]
    distance = tupleDist[1]
    return volcano[valve]['flow'] * (i-distance-1)


pos = 'AA'
for i in range(30, 0, -1):
    valves = volcano[pos]['distances']
    gains = list(map(calculGain, volcano[pos]['distances']))
    nextValve = valves[gains.index(max(gains))]

print(volcano)