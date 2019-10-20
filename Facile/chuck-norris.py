import sys
import math
import itertools

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def unarize(binary):
    series = [''.join(g) for k, g in itertools.groupby(binary)]
    unary = ""
    for s in series:
        if '1' in s:
            unary += "0 "
        elif '0' in s:
            unary += "00 "
        for i in range(len(s)):
            unary += "0"
        unary += " "
    return unary[:-1]
    
message = input()
binary = ''.join(format(ord(x), '07b') for x in message)
print(unarize(binary))