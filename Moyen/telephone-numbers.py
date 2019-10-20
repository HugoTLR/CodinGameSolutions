import sys
import math


cpt = 0

class Node:
    def __init__(self,i,val):
        self.i = i
        self.v = val
        self.s = []
        self.d = False
        
    def __str__(self):
        res = ""
        res += str(self.v) + ": {} sons    ".format(len(self.s))
        for s in self.s:
            res += s.__str__()
        return res

    def count(self):
        score = 0
        if self.d == False:
            score += 1
            self.d = True
        for ss in self.s:
            score += ss.count()
        return score
                    

def constructTree(roots,telephone):
    
    actuNode = next( (n for n in roots if n.v == int(telephone[0])),None)
    global cpt
    if actuNode == None:
        actuNode = Node(cpt,int(telephone[0]))
        cpt += 1
        roots.append(actuNode)
    
    
    for i in range(1,len(telephone)):
        nextNode = next( (n for n in actuNode.s if n.v == int(telephone[i])),None)
        if nextNode == None:
            nextNode = Node(cpt,int(telephone[i]))
            cpt += 1
            actuNode.s.append(nextNode)
        actuNode = nextNode
    
    return roots
        

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

roots = []

n = int(input())
for i in range(n):
    telephone = [int(t) for t in input()]
    print(telephone,file=sys.stderr)
    
    roots = constructTree(roots,telephone)

finalScore = 0
for r in roots:
    finalScore += r.count()
print(finalScore)
