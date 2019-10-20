import sys
import math


def calcSize(n):
    cpt = 1
    for _ in range(n-1):
        cpt += 2
    return cpt
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())

l = [[' ' for i in range((2*calcSize(n))+1)] for j in range(2*n)]
l[0][0] = '.'

for j in range(n):
    if j == 0:
        l[j][int(len(l[j])/2)] = '*'
    else:
        for i in range(len(l[j])):
            if i != 0 and  l[j-1][i-1] == '*':
                l[j][i] = '*'
            if i != len(l[j])-1 and  l[j-1][i+1] == '*':
                l[j][i] = '*'
            if  l[j-1][i] == '*':
                l[j][i] = '*'
                
for j in range(n,2*n):
    for i in range(len(l[j])):
            if i != 0 and  l[j-1][i-1] == '*':
                l[j][i] = '*'
            if i != len(l[j])-1 and  l[j-1][i+1] == '*':
                l[j][i] = '*'
            if  l[j-1][i] == '*':
                l[j][i] = '*'
    if j == n:
        indexes = [i for i, e in enumerate(l[j]) if e == '*']
        for i in range(len(indexes)):
            if i != 0 and i != len(indexes)-1:
                l[j][indexes[i]] = ' '
        
        
for ll in l:
    lastStarId = [i for i, e in enumerate(ll) if e == '*'][-1]
    ll = ll[:lastStarId+1]
    print(''.join(ll))