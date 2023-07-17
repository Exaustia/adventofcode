
arbo = {}
parents = ['/']

def addFile(sousArbo, parents, file, size):
    if len(parents) == 1:
        sousArbo[file] = size
    else:
        addFile(sousArbo[parents[1]], parents[1:], file, size)

def addFolder(sousArbo, parents, folder):
    if len(parents) == 1:
        sousArbo[folder] = {}
    else:
        addFolder(sousArbo[parents[1]], parents[1:], folder)


with open('./Kapy/day07/input.txt', 'r') as f:
    for line in f.readlines():
        line = line.strip()
        if line != '$ cd /' and line != '$ ls': # ignore these
            if line == '$ cd ..': 
                parents.pop()
            elif line[0] == '$': # '$ cd dir'
                dir = line[5:]
                parents.append(dir)
            else: 
                if line[0:3] == 'dir': # folder
                    folder = line[4:]
                    addFolder(arbo, parents, folder)
                else: # file
                    size, file = line.split(' ')
                    addFile(arbo, parents, file, int(size))

def getSize(arbo):
    i = 0
    for x in arbo:
        if type(arbo[x]) == type({}): # folder
            i += getSize(arbo[x])
        else: # file
            i += arbo[x]
    return i    

def getP1(arbo):
    total = 0
    for x in arbo:
        if type(arbo[x]) == type({}): # folder
            size = getSize(arbo[x])
            if size <= 100000:
                total += size
            total += getP1(arbo[x])
    return total

print(getP1(arbo))