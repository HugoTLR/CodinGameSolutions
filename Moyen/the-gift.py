import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
c = int(input())
budget = sorted([int(input()) for _ in range(n)])



# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
if sum(budget) < c:
    print("IMPOSSIBLE")
else:
    cpt = 0
    for b in budget:
        meanPart = c/(n-cpt)
        if b < meanPart:
            print(b)
            c -= b
        else:
            print(int(meanPart))
            c -= int(meanPart)
        cpt += 1