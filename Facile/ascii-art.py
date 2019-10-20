import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def formatRes(t,asciiTable,l,h):
    res = ""
    idLettres= []
    for i in range(len(t)):
        numLettre = ord(t[i]) - 64
        if numLettre < 1:
            numLettre = 0
        idLettres.append(int(numLettre))
        
        
    
    print(idLettres,file=sys.stderr)
    
    
    for k in range(0,h):
        for j in idLettres:
            for m in range((j-1)*l,(j)*l):
                res += asciiTable[k][m]
        res += "\n"
    return res

l = int(input())
h = int(input())
t = input()

asciiTable = []
for i in range(h):
    row = input()
    asciiTable.append(row)

for r in asciiTable:
    print(r,file=sys.stderr)
t = t[:].upper()
res = formatRes(t,asciiTable,l,h)

print(res)