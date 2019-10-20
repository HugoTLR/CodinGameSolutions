import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
LEFT = 0
TOP = 1
RIGHT = 2
BOT = 3

pieceDic = {}
pieceDic[0] = []
pieceDic[1] = [(LEFT,BOT),(TOP,BOT),(RIGHT,BOT)]
pieceDic[2] = [(LEFT,RIGHT),(RIGHT,LEFT)]
pieceDic[3] = [(TOP,BOT)]
pieceDic[4] = [(TOP,LEFT),(RIGHT,BOT)]
pieceDic[5] = [(TOP,RIGHT),(LEFT,BOT)]
pieceDic[6] = [(LEFT,RIGHT),(RIGHT,LEFT)]
pieceDic[7] = [(TOP,BOT),(RIGHT,BOT)]
pieceDic[8] = [(LEFT,BOT),(RIGHT,BOT)]
pieceDic[9] = [(LEFT,BOT),(TOP,BOT)]
pieceDic[10] = [(TOP,LEFT)]
pieceDic[11] = [(TOP,RIGHT)]
pieceDic[12] = [(RIGHT,BOT)]
pieceDic[13] = [(LEFT,BOT)]


dirToValueDic = {}
dirToValueDic[LEFT] = (-1,0)
dirToValueDic[TOP] = (0,-1)
dirToValueDic[RIGHT] = (+1,0)
dirToValueDic[BOT] = (0,+1)


# w: number of columns.
# h: number of rows.
w, h = [int(i) for i in input().split()]

grid = [[0 for _ in range(w)]for _ in range(h)]

for i in range(h):
    line = input()  # represents a line in the grid and contains W integers. Each integer represents one room of a given type.
    vals = line.split(' ')
    for l in range(len(vals)):
        grid[i][l] = int(vals[l])

        
ex = int(input())  # the coordinate along the X axis of the exit (not useful for this first mission, but must be read).

# game loop
while True:
    xi, yi, pos = input().split()
    xi = int(xi)
    yi = int(yi)
    f = -1
    if pos == "LEFT":
        f = 0
    elif pos == "TOP":
        f = 1
    else:
        f = 2
    for t in pieceDic[grid[yi][xi]]:
        if f == t[0]:
            subs = dirToValueDic[t[1]]
    xi += subs[0]
    yi += subs[1]
    
    print(str(xi) + " " + str(yi))