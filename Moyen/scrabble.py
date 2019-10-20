import sys
import math
from operator import itemgetter

def isDoable(word,letters):
    tmpLettters = letters.copy()
    for w in word:
        if w in tmpLettters:
            tmpLettters.remove(w)
        else:
            return False
    return True
    
def score(word,scoreDic):
    sc = 0
    for w in word:
        if w in scoreDic[1]:
            sc += 1
        elif w in scoreDic[2]:
            sc += 2
        elif w in scoreDic[3]:
            sc += 3
        elif w in scoreDic[4]:
            sc += 4
        elif w in scoreDic[5]:
            sc += 5
        elif w in scoreDic[8]:
            sc += 8
        elif w in scoreDic[10]:
            sc += 10
    return sc
    

scoreDic = {}
scoreDic[1] = ['e','a','i','o','n','r','t','l','s','u']
scoreDic[2] = ['d','g']
scoreDic[3] = ['b','c','m','p']
scoreDic[4] = ['f','h','v','w','y']
scoreDic[5] = ['k']
scoreDic[8] = ['j','x']
scoreDic[10] = ['q','z']

wordsIdToScore = {}
wordsIdToWord = {}


n = int(input())
words = []
cpt = 0
for i in range(n):
    w = input()
    if len(w) <= 7:
        wordsIdToScore[cpt] = score(w,scoreDic)
        wordsIdToWord[cpt] = w
        cpt += 1
letters = input()
letters = [l for l in letters]

wordsIdToScore = sorted(wordsIdToScore.items(), key=itemgetter(1),reverse=True)

for k in wordsIdToScore:
    if isDoable(wordsIdToWord[k[0]],letters):
        print(wordsIdToWord[k[0]])
        break
