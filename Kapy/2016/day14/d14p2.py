import hashlib
import re

def hashThis(txt):
    for _ in range(2017):
        txt = hashlib.md5(txt.encode('utf-8')).hexdigest()
    return txt

i = 0
nbKeys = 0
lookfor = []
hashList = []
salt = open('./2016/day14/input.txt', 'r').read()
while(nbKeys < 64):
    i += 1
    if i > len(hashList):
        hash = hashThis(salt + str(i))
        hashList.append(hash)
    else:
        hash = hashList[i-1]
    s = re.search(r'(.)\1\1', hash)
    if s:
        for j in range(1000):
            if i+j+1 > len(hashList):
                hash = hashThis(salt + str(i+j+1))
                hashList.append(hash)
            else:
                hash = hashList[i+j]
            if re.search(s.group()[0]*5,hash):
                nbKeys += 1
                break
print(i)