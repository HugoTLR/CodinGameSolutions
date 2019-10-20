import sys
import math



def computeNewPos(bat_pos,bomb_dir,top,bot,left,right):
    x = 0
    y = 0
    if bomb_dir == "L":
        print("Bomb on Left!",file=sys.stderr)
        top = bat_pos[1]
        bot = top
        right = bat_pos[0]
    elif bomb_dir == "R":
        print("Bomb on Right!",file=sys.stderr)
        top = bat_pos[1]
        bot = top
        left = bat_pos[0]
    elif bomb_dir == "U":
        print("Bomb on Top!",file=sys.stderr)
        left = bat_pos[0]
        right = left
        bot = bat_pos[1]
    elif bomb_dir == "D":
        print("Bomb on Bot!",file=sys.stderr)
        left = bat_pos[0]
        right = left
        top = bat_pos[1]
    elif bomb_dir == "UR":
        print("Bomb on TopRight!",file=sys.stderr)
        left = bat_pos[0]
        bot = bat_pos[1]
    elif bomb_dir == "UL":
        print("Bomb on TopLeft!",file=sys.stderr)
        right = bat_pos[0]
        bot = bat_pos[1]
    elif bomb_dir == "DR":
        print("Bomb on BotRight!",file=sys.stderr)
        left = bat_pos[0]
        top = bat_pos[1]
    else:        
        print("Bomb on BotLeft!",file=sys.stderr)
        right = bat_pos[0]
        top = bat_pos[1]
    x = int((left+right)/2)
    y = int((top+bot)/2)
    return (x,y),top,bot,left,right
    
# w: width of the building.
# h: height of the building.
w, h = [int(i) for i in input().split()]

print("WIDTH: {},HEIGHT: {}".format(w,h), file=sys.stderr)

n = int(input())  # maximum number of turns before game over.
x0, y0 = [int(i) for i in input().split()]
batPos = (x0,y0)

top = 0
bot = h
left = 0
right = w

# game loop
while True:
    bomb_dir = input()  # the direction of the bombs from batman's current location (U, UR, R, DR, D, DL, L or UL)
    # Write an action using print
    # To debug: print
    batPos,top,bot,left,right = computeNewPos(batPos,bomb_dir,top,bot,left,right)


    # the location of the next window Batman should jump to.
    print(str(batPos[0])+ " " + str(batPos[1]))