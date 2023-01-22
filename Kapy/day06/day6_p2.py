
def isMarker(x):
    return len(set(x)) == len(x)

with open('./Kapy/day06/input.txt', 'r') as f:
    input = f.read()
    for i in range(0,len(input)):
        if isMarker(input[i:i+14]): # start of message Marker
            print(i+14)
            break