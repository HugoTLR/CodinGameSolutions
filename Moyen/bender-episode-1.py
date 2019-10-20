import sys
import math

def doStep1(cartes1,cartes2,c1=[],c2=[],fin = False):
    if fin:
        return cartes1, cartes2,fin
        
    
    c1.append(cartes1.pop(0))
    c2.append(cartes2.pop(0))
    
    if cardToValDic[c1[-1][:-1]] > cardToValDic[c2[-1][:-1]]:
        cartes1.extend(c1)
        cartes1.extend(c2)
    elif cardToValDic[c1[-1][:-1]] < cardToValDic[c2[-1][:-1]]:
        cartes2.extend(c1)
        cartes2.extend(c2)
    else:
        if len(cartes1) < 4 or len(cartes2) < 4:
            fin = True
        else:
            c1.extend([cartes1.pop(0) for _ in range(3)])
            c2.extend([cartes2.pop(0) for _ in range(3)])
            cartes1, cartes2,fin = doStep1(cartes1,cartes2,c1,c2,fin)
    
     
    
    
    return cartes1,cartes2,fin
    
    
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

n = int(input())  # the number of cards for player 1
cardp_1 = []
for i in range(n):
    cardp_1.append(input())  # the n cards of player 1
m = int(input())  # the number of cards for player 2
cardp_2 = []
for i in range(m):
    cardp_2.append(input())  # the m cards of player 2
    
cardToValDic = {}
for i in range(2,11):
    cardToValDic[str(i)] = i
cardToValDic['J'] = 11
cardToValDic['Q'] = 12
cardToValDic['K'] = 13
cardToValDic['A'] = 14

print(cardToValDic, file=sys.stderr)

cpt = 0
fin = False
while not fin:
    print((cardp_1,cardp_2), file=sys.stderr)
    cardp_1,cardp_2,fin = doStep1(cardp_1,cardp_2,list(),list())
    cpt += 1
    if len(cardp_1) == 0 or len(cardp_2) == 0 or fin:
        if fin:
            print("PAT")
        elif len(cardp_1) == 0:
            print("2 {}".format(cpt))
        else:
            print("1 {}".format(cpt))
        fin = True
            
            
# Write an action using print
# To debug: print("Debug messages...", file=sys.stderr)
