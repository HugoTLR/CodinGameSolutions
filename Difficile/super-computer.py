import sys
import math
import numpy as np

activityList = []
n = int(input())
for i in range(n):
    j, d = [int(j) for j in input().split()]
    activityList.append((j,j+d))

activityList = sorted(activityList, key= lambda x: x[1])
score = 1
lastActi = activityList.pop(0)
for acti in activityList:
    if acti[0] >= lastActi[1]:
        score += 1
        lastActi = acti
print(score)