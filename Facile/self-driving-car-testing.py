import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
xthen_commands = input()
pos = xthen_commands.split(';')[0]
pos = int(pos) -1 
moveDic = {}
cpt = 0
for i in xthen_commands.split(';')[1:]:
    moveDic[cpt] = {"nb": int(i[:-1]),"dir": i[-1]}
    cpt += 1
    
roadDic = {}
for i in range(n):
    rthen_roadpattern = input()
    roadDic[i] = {"nb":int(rthen_roadpattern.split(';')[0]), "list": [c for c in rthen_roadpattern.split(';')[1]]}
    
keyMove = 0
moveCpt = 0
for k,v in roadDic.items():
    for i in range(v["nb"]):
        if moveDic[keyMove]["dir"] == "L":
            pos -= 1
        elif moveDic[keyMove]["dir"] == "R":
            pos += 1
        tmpCh = v["list"][pos]
        v["list"][pos] = '#'
        moveCpt += 1
        if moveCpt == moveDic[keyMove]["nb"]:
            keyMove += 1
            moveCpt = 0
        print(''.join(v["list"]))
        
        v["list"][pos] = tmpCh

