import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
j = int
s = sorted
n = j(input())
values = [j(i) for i in input().split()]


cpt = 0
biggestLoss = 0
lv = -sys.maxsize
while values:
    v = values.pop(0)
    if v < lv:
        continue
    
    baddays = s(values)
    if baddays:
        low = baddays[0]
        if low-v < biggestLoss:
            biggestLoss = low-v
    lv = v

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(biggestLoss)