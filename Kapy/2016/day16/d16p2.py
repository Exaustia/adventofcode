import re

def swap(s):
    n = int(s, 2)
    n = ~n & ((1 << len(s)) - 1) # NOT n AND int('1'*(len(s)),2)
    s = bin(n)[2:].zfill(len(s)) # [2:] to skip 0b at the start
    return s

def checksum(s):
    while(len(s) % 2 == 0):
        s = ''.join([str(int(s[i*2]==s[i*2+1])) for i in range(int(len(s)/2))])
    return s
        
data = open('./2016/day16/input.txt', 'r').read()
while(len(data) < 35651584):
    data = data + '0' + swap(data[::-1])
print(checksum(data[:35651584]))