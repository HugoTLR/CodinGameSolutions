import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.



n = int(input())  # Number of elements which make up the association table.
q = int(input())  # Number Q of file names to be analyzed.

mimeTypeDic = {}

for i in range(n):
    # ext: file extension
    # mt: MIME type.
    ext, mt = input().split()
    mimeTypeDic[ext.lower()] = mt

printList = []
for i in range(q):
    fname = input()  # One file name per line.
    st = fname.split('.')
    if len(st) >= 2 and st[-1].lower() in mimeTypeDic.keys():
        printList.append(mimeTypeDic[st[-1].lower()])
    else:
        printList.append("UNKNOWN")

# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)

for l in printList:
    print(l)