import sys
import math
import statistics
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

houses = {}
h_cable_y = 0
h_cablesize = 0
min_X=  sys.maxsize
max_X = -sys.maxsize
n = int(input())
for i in range(n):
    
    x, y = [int(j) for j in input().split()]
    if x < min_X:min_X = x
    if x > max_X:max_X = x
    houses[i] =(y,x)
    
h_cable_y = int(statistics.median([v[0] for k,v in houses.items()]))
h_cablesize = max_X-min_X
v_cablesize=0
for k,v in houses.items():
    v_cablesize += abs(v[0]-h_cable_y)

print(h_cablesize+v_cablesize)