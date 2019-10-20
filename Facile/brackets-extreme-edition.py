import sys
import math

class SuperChar:
    def __init__(self,c,i,s,opener=True):
        self.c = c
        self.o = opener
        self.i = i
        self.s = s
        
    def __str__(self):
        return self.c
    
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

expression = input()
#print(expression,file=sys.stderr)

allChar = [SuperChar('{',0,5),
                SuperChar('(',1,4),
                SuperChar('[',2,3),
                SuperChar(']',3,2,False),
                SuperChar(')',4,1,False),
                SuperChar('}',5,0,False)]

g = True
unclosedChar = []
for e in expression:
    if e not in [a.c for a in allChar]:
        continue
    ch = [a for a in allChar if a.c == e][0]
    avaiableChar = [a for a in allChar if (len(unclosedChar) == 0 or a.o or unclosedChar[-1].s == a.i )]
    #print("avai:{}\t -> output -> {}".format([a.__str__() for a in avaiableChar],ch),file=sys.stderr)
    if ch not in avaiableChar:
        g = False
        break
        
    if ch.o:
        unclosedChar.append(ch)
    else:
        if len(unclosedChar) == 0 or unclosedChar[-1].s != ch.i:
            g = False
            break
        del unclosedChar[-1]

if len(unclosedChar) > 0:
    g = False
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
print("true") if g else print("false")