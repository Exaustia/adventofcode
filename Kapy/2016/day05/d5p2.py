import hashlib

id = open('./2016/day05/input.txt', 'r').read()
pwd = ['#']*8
i = 0
while True:
    hash = hashlib.md5((id+str(i)).encode('utf-8')).hexdigest()
    if hash.startswith('00000'):
        if hash[5].isdigit():
            pos = int(hash[5])
            if pos < 8:
                if pwd[pos] == '#':
                    pwd[pos] = hash[6]
                    if '#' not in pwd:
                        break
    i += 1
print(''.join(pwd))