import re

def getSum(ob):
    if type(ob) is int:
        return ob
    elif type(ob) is str:
        return 0
    elif type(ob) is list:
        sum = 0
        for x in ob:
            sum += getSum(x)
        return sum
    else:
        sum = 0
        for x in ob.values():
            if x == 'red':
                return 0
            else:
                sum += getSum(x)
        return sum

ob = eval(open('./2015/day12/input.txt', 'r').read())
print(getSum(ob))