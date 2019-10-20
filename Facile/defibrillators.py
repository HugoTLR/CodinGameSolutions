import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def cDist(lon,lat,lon2,lat2):
    x = (lon2 - lon) * math.cos((lat+lat2)/2 )
    y = (lat2-lat)
    return math.sqrt((x**2)+(y**2)) * 6371

lon = math.radians(float(input().replace(",",".")))
lat = math.radians(float(input().replace(",",".")))
n = int(input())


defibDicList = {}

for i in range(n):
    defib = input()
    attr = defib.split(";")
    dic = {}
    idD = int(attr[0])-1
    dic["name"] = attr[1]
    dic["addr"] = attr[2]
    dic["num"] = attr[3]
    dic["lon"] = math.radians(float(attr[4].replace(",",".")))
    dic["lat"] = math.radians(float(attr[5].replace(",",".")))
    defibDicList[idD] = dic

closestDist = 100000000000
closestId = -1
for k,v in defibDicList.items():
    dist = cDist(lon,lat,v["lon"],v["lat"])
    if dist < closestDist:
        closestDist = dist
        closestId = k        

print(defibDicList[closestId]["name"])