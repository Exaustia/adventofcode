import re

input = open('./2015/day12/input.txt', 'r').read()
nbList = [int(x) for x in re.findall('-?\\d+', input)]
print(sum(nbList))