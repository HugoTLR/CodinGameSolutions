import sys
import math
from itertools import combinations
import numpy as np

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())
ar = np.zeros((n),dtype=int)
for i in range(n):
    pi = int(input())
    ar[i] = pi

ar = sorted(ar)
minP = 10000
lastV = 10000
for i in ar:
    d = abs(i-lastV)
    if d < minP:
        minP = d
    lastV = i


# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

print(minP)