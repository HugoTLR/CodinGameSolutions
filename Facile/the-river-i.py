import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def calcNext(r):
    v = str(r)
    
    for x in v:
        r += int(x)
    return r

r_1 = int(input())
r_2 = int(input())

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)


while True:
    
    if r_1 < r_2:
        r_1 = calcNext(r_1)
    elif r_1 > r_2:
        r_2 = calcNext(r_2)
        
    if r_1 == r_2:
        print(r_1)
        break