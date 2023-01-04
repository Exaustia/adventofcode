def draw():
    txt = ''
    for y in range(highest, -1, -1):
        for x in range(9):
            if x in [0, 8] or (x, y) in obstacles:
                txt += '#'
            else:
                txt += '.'
        txt += '\n'
    print(txt)