import hashlib

id = open('./2016/day05/input.txt', 'r').read()
pwd = ''
for i in range(100000000):
    hash = hashlib.md5((id+str(i)).encode('utf-8')).hexdigest()
    if hash.startswith('00000'):
        pwd += hash[5]
        if len(pwd) == 8:
            break
print(pwd)