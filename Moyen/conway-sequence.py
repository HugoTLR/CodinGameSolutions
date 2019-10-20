import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def newList(oldList):
    modu = 0
    cpt = 0
    res = []
    
    sameItemList = 0
    lastItem = -1
    
    if len(oldList) == 1:
        res.append(1)
        res.append(oldList[0])
        
    else:
        for i in oldList:
            if sameItemList == 0:
                sameItemList += 1
                lastItem = i
            else:
                if lastItem == i:
                    sameItemList += 1
                else:
                    res.append(sameItemList)
                    res.append(lastItem)
                    sameItemList = 1
                    lastItem = i
        res.append(sameItemList)
        res.append(lastItem)
    return res
            
            

def compute(r,l):
    lines = []
    lines.append([])
    lines.append([r])
    for i in range(2,l+1):
        #print("lines[-1]: {}".format(lines[-1]), file=sys.stderr)
        lines.append(newList(lines[-1]))
    return lines[-1]

def printRes(res):
    string = str(res[0])
    for r in range(1,len(res)):
        string += " "
        string += str(res[r])
    return string

r = int(input())
l = int(input())

print("r:{}\tl:{}".format(r,l), file=sys.stderr)
res = compute(r,l)
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(printRes(res))