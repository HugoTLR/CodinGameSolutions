import sys
import math


def grabNb(pos,w,h):
    
    nb = []
    for j in range(pos[0]-1,pos[0]+2):
        for i in range(pos[1]-1,pos[1]+2):
            if j >= 0 and j < h:
                if i >= 0 and i < w:
                    if j != pos[0] or i != pos[1]:
                        nb.append((j,i))
    return nb
                    
            
    

width, height = [int(i) for i in input().split()]

dmap = []
for i in range(height):
    line = input()
    x = [int(c) for c in line]
    dmap.append(x)

finalDmap = [[0 for i in range(width)] for j in range(height)]
for j in range(height):
    for i in range(width):
        nb = grabNb( (j,i),width,height)
        aliveNb = len([ n for n in nb if dmap[n[0]][n[1]] == 1 ])
        if dmap[j][i] == 1:
            if aliveNb < 2 or aliveNb > 3:
                finalDmap[j][i] = 0
            else:
                finalDmap[j][i] = 1
        else:
            if aliveNb == 3:
                finalDmap[j][i] = 1
 

for d in finalDmap:
    print(''.join([str(c) for c in d]))