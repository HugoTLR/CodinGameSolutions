import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def walk(dmap,startPoint):
    startIndex = [d[0] for d in dmap].index(startPoint)
    
    actuPos = [startIndex,0]
    while True:
        actuPos[1] += 1
        if actuPos[0] != 0:
            if dmap[actuPos[0]-1][actuPos[1]] == '-':
                actuPos[0] -= 3
                continue
        if actuPos[0] != len(dmap)-1:
            if dmap[actuPos[0]+1][actuPos[1]] == '-':
                actuPos[0] += 3
                continue
        
        if actuPos[1] == len(dmap[0]) -1:
            break
    return dmap[actuPos[0]][actuPos[1]]
            

def rotated(array_2d):
    list_of_tuples = zip(*array_2d[::-1])
    return [list(elem) for elem in list_of_tuples]
    
w, h = [int(i) for i in input().split()]

dmap = []
entryList = []
for i in range(h):
    line = input()
    if i == 0:
        entryList = [c for c in line if c != ' ']
    dmap.append([c for c in line])

dmap = dmap[::-1]
dmap = rotated(dmap)

for e in entryList:
    print("{}{}".format(e,walk(dmap,e)))

