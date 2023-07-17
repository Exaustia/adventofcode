import re

def swap(s):
    n = int(s, 2)
    n = ~n & ((1 << len(s)) - 1) # NOT n AND int('1'*(len(s)),2)
    s = bin(n)[2:].zfill(len(s)) # [2:] to skip 0b at the start
    return s

def checksum(s):
    while(len(s) % 2 == 0):
        r = re.search('(..)'*int(len(s)/2), s)
        s = ''.join([str(int(pair[0]==pair[1])) for pair in r.groups()])
    return s

data = open('./2016/day16/input.txt', 'r').read()
while(len(data) < 272):
    data = data + '0' + swap(data[::-1])
print(checksum(data[:272]))