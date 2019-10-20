import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.


def calcNext(r):
    v = str(r)
    for x in v:
        r += int(x)
    return r


# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

r_1 = int(input())

c = calcNext
yes = False
for i in range(r_1-1,1,-1):
    if c(i) == r_1:
        yes = True
        break


print("YES") if yes else print("NO")