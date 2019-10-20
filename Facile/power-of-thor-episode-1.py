import sys
import math

def computeMoveQueue(initPos,objPos):
    deltaX = initPos[0]-objPos[0] ## OBJ on right if X < 0
    deltaY = initPos[1]-objPos[1] ## OBJ on top if Y > 0
    queue = []
    while deltaX != 0 or deltaY != 0:
        if deltaX < 0:
            if deltaY > 0:
                queue.append("NE")
                deltaX += 1
                deltaY -= 1
            elif deltaY < 0:
                queue.append("SE")
                deltaX += 1
                deltaY += 1
            else:
                queue.append("E")
                deltaX += 1
        elif deltaX > 0:
            if deltaY > 0:
                queue.append("NW")
                deltaX -= 1
                deltaY -= 1
            elif deltaY < 0:
                queue.append("SW")
                deltaX -= 1
                deltaY += 1
            else:
                queue.append("W")
                deltaX -= 1
        else:
            if deltaY > 0:
                queue.append("N")
                deltaY -= 1
            else:
                queue.append("S")
                deltaY += 1
            
    return queue

# light_x: the X position of the light of power
# light_y: the Y position of the light of power
# initial_tx: Thor's starting X position
# initial_ty: Thor's starting Y position
light_x, light_y, initial_tx, initial_ty = [int(i) for i in input().split()]
moveQueue = computeMoveQueue((initial_tx,initial_ty),(light_x,light_y))
i = 0
# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move. Do not remove this line.
    print(moveQueue[i])
    i+=1