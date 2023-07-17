import re

def decompress(txt):
    n = 0
    while True:
        s = re.search(r'\((\d+)x(\d+)\)', txt)
        if s:
            i,l = s.span() # start, end of match
            a,b = int(s.groups()[0]), int(s.groups()[1]) 
            n += i + decompress(txt[l:l+a])*b
            txt = txt[a+l:] # start the string later
        else:
            break
    return n+len(txt)

print(decompress(open('./2016/day09/input.txt', 'r').read()))