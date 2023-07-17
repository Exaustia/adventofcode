import hashlib

input = open('./2015/day04/input.txt', 'r').read()
for i in range(1000000):
    hash = hashlib.md5((input+str(i+1)).encode('utf-8')).hexdigest()
    if str(hash).startswith('00000'):
        break
print(i+1)