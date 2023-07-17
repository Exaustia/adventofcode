
def look_and_say(nb):
    y = ''
    x = 1
    for i in range(len(nb)):
        if i < len(nb)-1:
            if nb[i] == nb[i+1]:
                x += 1
                continue        
        y += str(x)+str(nb[i])
        x = 1
    return y        

result = open('./2015/day10/input.txt', 'r').read()
for _ in range(40):
    result = look_and_say(result)
print(len(result))