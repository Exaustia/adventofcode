
import math

def unSNAFU(snafu):
    nb = 0
    for i, d in enumerate(snafu[::-1]):
        d = int(d) if d in ('0','1','2') else -1 if d == '-' else -2
        nb += d*(5**i)
    return nb

def toSNAFU(nb):
    snafu = ''
    maxPow = maxPow5(nb)
    while maxPow >= 0:
        multi = math.trunc(nb/(5**maxPow))
        nb -= multi*(5**maxPow)
        if multi <= 2:
            snafu += str(multi)
        else:
            if len(snafu) > 0:
                snafu = snafu[:-1] + snafuList[snafuList.index(snafu[-1]) - 1]
            else:
                snafu = '1'
            snafu += '=' if multi == 3 else '-'
        maxPow -= 1
    return snafu

def maxPow5(nb):
    if nb == 0:
        return 0
    else:
        power = 1
        i = 0
        while power <= nb:
            power *= 5
            i += 1
        return i-1

snafuList = ['2', '1', '0', '-', '=']
total = 0
for nb in open('./Kapy/day25/input.txt', 'r').read().split('\n'):
    total += unSNAFU(nb)

print(toSNAFU(total))