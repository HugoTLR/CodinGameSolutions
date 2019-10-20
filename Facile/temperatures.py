import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of temperatures to analyse

def returnBestVal(tempList):
    bTemp = []
    bId = -1
    bAbs = 10000
    for t in tempList:
        if abs(t-0) <= bAbs:
            bAbs = abs(t-0)
            bTemp.append(t)
    return str(sorted(bTemp,reverse=True)[0]) if bTemp else 0

tempList = []
for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    tempList.append(t)
tempList.sort()
print(returnBestVal(tempList))