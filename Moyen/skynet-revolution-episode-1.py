import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

class Node:
    
    def __init__(self,id):
        self.id = id
        self.link = []
        self.exit = False
        self.tag = False
        
    def __str__(self):
        return "Id:{}\tExit:{}\tLink:{}".format(self.id,self.exit,self.link)
        
        
def parcoursLargeur(nodeDic,rootId=0):
    f = [nodeDic[rootId]]
    nodeDic[rootId].tag = True
    
    dangerousLink = []
    while len(f) > 0:
        s = f.pop(0)
        #print(s, file=sys.stderr)
        
        for n in s.link:
            if not nodeDic[n].tag:
                f.append(nodeDic[n])
                nodeDic[n].tag = True
            if nodeDic[n].exit:
                dangerousLink.append((s.id,nodeDic[n].id))
    for k,v in nodeDic.items():
        v.tag = False
    return dangerousLink
    
# n: the total number of nodes in the level, including the gateways
# l: the number of links
# e: the number of exit gateways
n, l, e = [int(i) for i in input().split()]



nodeDic = {}
for i in range(n):
    nodeDic[i] = Node(i)
    

for i in range(l):
    # n1: N1 and N2 defines a link between these nodes
    n1, n2 = [int(j) for j in input().split()]
    nodeDic[n1].link.append(n2)
    nodeDic[n2].link.append(n1)
for i in range(e):
    ei = int(input())  # the index of a gateway node
    nodeDic[ei].exit = True
    
for k,v in nodeDic.items():
    v.link.sort()
    #print(v.__str__(),file=sys.stderr)


# game loop
while True:
    si = int(input())  # The index of the node on which the Skynet agent is positioned this turn
    dangerousLink = parcoursLargeur(nodeDic.copy(),si)
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    #print(dangerousLink,file=sys.stderr)

    # Example: 0 1 are the indices of the nodes you wish to sever the link between
    print(str(dangerousLink[0][0]) + " " + str(dangerousLink[0][1]))