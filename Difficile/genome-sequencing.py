import sys
import math


         
n = int(input())
SUBSEQS = [input() for _ in range(n)]
SMALLEST_CHAIN = sys.maxsize

def solve(seq,lis,minWin=sys.maxsize):
    if not lis:
        return minWin
    seq2 = lis.pop(0)
    new_words = linkable(seq,seq2)
    winner_words = []
    for n in new_words:
        w = True
        for s in SUBSEQS:
            if s not in n:
                w = False;break
        if w:
            winner_words.append(n)
    if winner_words:
        w = sorted(winner_words,key=lambda x: len(x))[0]
        if len(w) < minWin:
            minWin = len(w)
    
    for n in new_words:
        v = solve(n,[l for l in lis],minWin)
        if v < minWin:
            minWin = v
    return minWin



def linkable(seq1,seq2):
    size = min(len(seq1),len(seq2))
    f1,f2 = False,False
    links = []
    for i in range(1,size+1,1):
        if seq1[-i:] in seq2[:i]:
            new_word = seq1[:-i]+seq2
            links.append(new_word)
            f1 = True
            
        if seq2[-i:] in seq1[:i]:
            new_word = seq2[:-i]+seq1
            links.append(new_word)
            f2 = True
    if not f1:
        new_word = seq1+seq2
        links.append(new_word)
    if not f2:
        new_word = seq2+seq1
        links.append(new_word)
    return links

if n == 1:
    print(len(SUBSEQS[0]))
elif n == 2:
    if SUBSEQS[0] in SUBSEQS[1]: 
        print(len(SUBSEQS[1]))
    elif SUBSEQS[1] in SUBSEQS[0]: 
        print(len(SUBSEQS[0]))
    else:
        new_words = linkable(SUBSEQS[0],SUBSEQS[1])
        print(min([len(i) for i in new_words]))
else:
    for i in range(len(SUBSEQS)):
        lis = [s for s in SUBSEQS]
        seq1 = lis.pop(i)
        v = solve(seq1,lis)
        if v < SMALLEST_CHAIN:
            SMALLEST_CHAIN = v

    print(f"{SMALLEST_CHAIN}")
