import re

c = open('./2016/day09/input.txt', 'r').read()
n = 0
while True:
    s = re.search(r'\((\d+)x(\d+)\)', c)
    if s:
        i,l = s.span() # start, end of match
        a,b = int(s.groups()[0]), int(s.groups()[1]) 
        c = c[a+l:] # start the string later
        n += i + a*b
    else:
        break
print(n+len(c))