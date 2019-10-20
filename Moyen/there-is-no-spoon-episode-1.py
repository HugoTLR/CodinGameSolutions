import sys
import math

# Don't let the machines win. You are humanity's last hope...

width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis

nodeDic = {}
for i in range(height):
    line = input()  # width characters, each either 0 or .
    for j in range(len(line)):
        if line[j] == '0':
            nodeDic[(j,i)] = [(-1,-1),(-1,-1)]
            for k in range(j,len(line)):
                if k != width -1 and line[k+1] == '0':
                    nodeDic[(j,i)][0] = (k+1,i)
                    break
            for k in range(i,0,-1):
                if k > 0 and (j,k-1) in nodeDic:
                    nodeDic[(j,k-1)][1] = (j,i)
                    break

for k,v in nodeDic.items():
    print("{} {} {} {} {} {}".format(k[0],k[1],v[0][0],v[0][1],v[1][0],v[1][1]))
