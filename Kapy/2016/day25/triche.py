
n = 0
while(True):
    n += 1
    clock = ''
    a = n + 11*231
    while(a>0):
        a = int(a/2)
        c = a%2
        if clock == '' or clock[-1] != str(c):
            clock += str(c)
        else:
            clock = '-1'
            break
    
    if clock != '-1':
        print(n)
        break