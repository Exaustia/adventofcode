
def isValid(pwd):
    pairs = set()
    valid = True
    straight = pwd[0]
    for i, x in enumerate(pwd):
        if x in ['i', 'o', 'l']:
            valid = False
        if i > 0:
            pair = pwd[i-1] + pwd[i]
            if pair[0] == pair[1] and pair not in pairs:
                pairs.add(pair)
            if ord(straight[-1]) == ord(x)-1:
                straight += x
            elif len(straight) < 3:
                straight = x
    if len(straight) < 3 or len(pairs) < 2:
        valid = False
    return valid

def nextPwd(pwd):
    i = len(pwd)-1
    ok = False
    while(not(ok)):
        if pwd[i] == 'z':
            pwd = pwd[:i] + 'a' + pwd[i+1:]
            i -= 1
        else:
            pwd = pwd[:i] + chr(ord(pwd[i]) + 1) + pwd[i+1:]
            ok = True
    return pwd

pwd = open('./2015/day11/input.txt', 'r').read()

valid = False
while(not(valid)):
    pwd = nextPwd(pwd)
    valid = isValid(pwd)
valid = False
while(not(valid)):
    pwd = nextPwd(pwd)
    valid = isValid(pwd)

print(pwd)