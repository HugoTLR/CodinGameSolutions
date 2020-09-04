import sys
import math
import time

lacs = []

class pos:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def __eq__(self,other):
        return (self.x == other.x and self.y == other.y)
class cell(pos):
    def __init__(self,x,y,type):
        pos.__init__(self,x,y)
        self.type = type
    def __eq__(self,other):
        return pos.__eq__(self,other)
    def __str__(self):
        return self.type
class board:
    def __init__(self,b):
        self.board = b
    
    def __str__(self):
        res = ""
        for row in self.board:
            for r in row:
                res = res + r.__str__()
            res = res + "\n"
        return res + "\n"

        

l = int(input())
h = int(input())

WATERIN = False
LANDIN = False
CHECKED = [[False for _ in range(l)] for _ in range(h) ]
b = []
for i in range(h):
    row = input()
    j = 0
    line = []
    for r in row:
        if r == 'O':
            WATERIN = True
        if r == '#':
            LANDIN = True
        line.append(cell(j,i,r))
        j+=1
    b.append(line)

gameBoard = board(b)

n = int(input())
coords = []
for i in range(n):
    x, y = [int(j) for j in input().split()]
    coords.append((y,x))
    
    

def isInLac(coord):
    for l in lacs:
        if coord in l:
            return len(l)
    return -1

def getNeighbors(coord):
    nbs = []
    if coord[0] > 0 and CHECKED[coord[0]-1][coord[1]] == False:
        nbs.append((coord[0]-1,coord[1]))
    if coord[0] < h-1 and CHECKED[coord[0]+1][coord[1]] == False:
        nbs.append((coord[0]+1,coord[1]))
    if coord[1] > 0 and CHECKED[coord[0]][coord[1]-1] == False:
        nbs.append((coord[0],coord[1]-1))
    if coord[1] < l-1 and CHECKED[coord[0]][coord[1]+1] == False:
        nbs.append((coord[0],coord[1]+1))
    return nbs
        
def discover(coord):
    if gameBoard.board[coord[0]][coord[1]].type == '#':
        
        return 0
    else:
        lac = [coord]
        queu= lac.copy()
        qap = queu.append
        lap = lac.append
        while queu:
            current = queu.pop(0)
            CHECKED[current[0]][current[1]] = True
            nbs = getNeighbors(current)
            
            for n in nbs:
                if gameBoard.board[n[0]][n[1]].type == 'O':
                    lap(n)
                    qap(n)
                    CHECKED[n[0]][n[1]] = True
        lacs.append(lac)
        return len(lac)


for i in range(n):
    s = time.time()
    if not LANDIN:
        print(l*h)
    elif not WATERIN:
        print(0)
    else:
        #memo
        inLac = isInLac(coords[i])
        if inLac != -1:
            print(inLac)
        else:
            lenofnew = discover(coords[i])
            print(lenofnew)
    print(f"Coord checked in {time.time()-s} secs",file=sys.stderr)
