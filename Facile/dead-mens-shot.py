import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def hitOrMiss(cornerList,shot):

    pos = 0
    neg = 0
    
    for c in range(len(cornerList)):
        if cornerList[c] == shot:
            return True
        dot = 0
        if c == len(cornerList)-1:
            dot = (shot[0] - cornerList[c][0])*(cornerList[0][1] - cornerList[c][1]) - (shot[1] - cornerList[c][1]) * (cornerList[0][0] - cornerList[c][0])
        else:
            dot = (shot[0] - cornerList[c][0])*(cornerList[c+1][1] - cornerList[c][1]) - (shot[1] - cornerList[c][1]) * (cornerList[c+1][0] - cornerList[c][0])
        
        if dot > 0:
            pos += 1
        elif dot < 0:
            neg += 1
        if pos > 0 and neg > 0:
            return False
    return True

n = int(input())

cornerList = []
for i in range(n):
    x, y = [int(j) for j in input().split()]
    cornerList.append((x,y))

shotList = []
m = int(input())
for i in range(m):
    x, y = [int(j) for j in input().split()]
    shotList.append((x,y))


for s in shotList:
    print("hit") if hitOrMiss(cornerList,s) else print("miss")
# Write an action using print
