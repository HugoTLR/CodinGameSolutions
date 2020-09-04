import sys
import math

class checkpoint:
    def __init__(self,id,name,lat,lon,typ):
        self.id = id
        self.name = name
        self.latitude = lat
        self.longitude = lon
        self.type = typ
        self.f = sys.maxsize
        self.g = sys.maxsize
        self.cf = None

    def __str__(self):
        return f"{self.name}, {self.type}, {self.latitude}, {self.longitude}, g():{self.g}, f(): {self.f}"
    def __eq__(self,other=None):
        if other != None:
            return self.id == other.id
        else:
            return False
        
def calcDistance(cp1,cp2):
    x = (math.radians(cp2.longitude) - math.radians(cp1.longitude)) * math.cos( ( math.radians(cp1.latitude) + math.radians(cp2.latitude) ) / 2 )
    y = ( math.radians(cp2.latitude) - math.radians(cp1.latitude) )
    return math.sqrt(x**2 + y**2) * 6371

cpDic = {}
linkDic = {}
gScore = {}
fScore = {}
cameFrom = {}

start_point = input().split(':')[1]
end_point = input().split(':')[1]
n = int(input())
for i in range(n):
    stop_name = input()
    data = [i for i in stop_name.split(',') if i]
    cpDic[data[0].split(':')[1]] = checkpoint(data[0].split(':')[1],data[1][1:-1],float(data[2]),float(data[3]),int(data[4]))


m = int(input())
for i in range(m):
    route = input()
    links = [i.split(':')[1] for i in route.split(' ')]
    linkDic[' '.join(links)] = calcDistance(cpDic[links[0]],cpDic[links[1]])

def findNeighbors(current):
    neighbors= []
    for k in linkDic.keys():
        if current.id in k:
            l = k.split(' ')
            if l[0] == current.id:
                neighbors.append(cpDic[l[1]])
    return neighbors
                

def reconstruct_path(current):
    total_path = [f"{current.name}"]
    while True:
        if current.cf == None:
            break
        current = current.cf
        total_path = [f"{current.name}"] + total_path
    return total_path

def A_star():
    initList = [cpDic[start_point]]
    cpDic[start_point].g = 0
    cpDic[start_point].f = 1 
    while initList:
        initList = sorted(initList,key=lambda x: x.f)      
        current = initList.pop(0)
        if current.__eq__(cpDic[end_point]):
            return reconstruct_path(current)
        
        neighbors = findNeighbors(current)
        for n in neighbors:
            t_gScore = current.g + linkDic[' '.join([current.id,n.id])]
            if t_gScore < n.g:
                n.cf = current
                n.g = t_gScore
                n.f = n.g + 1
                if not n in initList:
                    initList.append(n)
    return []
    

if start_point == end_point:
    print(cpDic[start_point].name)
else:
    res = A_star()
    if res:
        for r in res:
            print(r)
    else:
        print("IMPOSSIBLE")
