import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def rotated(array_2d):
    list_of_tuples = zip(*array_2d[::-1])
    return [list(elem) for elem in list_of_tuples]

width, height = [int(i) for i in input().split()]
count = int(input())

dmap = []
for i in range(height):
    dmap.append([e for e in input()])

if count%2 == 1:
    for d in dmap:
        d.sort()
    dmap = dmap[::-1]
    dmap = rotated(dmap)
    dmap = dmap[::-1]
else:
    for d in dmap:
        d.sort(reverse=True)
    
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
for d in dmap:
    print(''.join([c for c in d]))