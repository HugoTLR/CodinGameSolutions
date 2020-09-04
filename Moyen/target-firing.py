import sys
import math

def solve(ships,beam_damage,shield):
    while ships:
        for ship in ships:
            shield -= ship._dmg
        ships = sorted(ships,key=lambda x: x._dmg/x._ttk,reverse=True)
        dmg_dealt = ships[0].target(beam_damage)
        ships[0].get_hit(dmg_dealt)

        ships = [s for s in ships if s._hp > 0]
        if shield < 0:
            break
    if shield >= 0:
        return shield
    return "FLEE"
        

class Ship:
    def __init__(self,_type,hp,armor,damage):
        self._type = _type
        self._hp = hp
        self._armor = armor
        self._dmg = damage
    
    def __str__(self):
        return f"Type:{self._type} Hp:{self._hp} Armor:{self._armor} Damage:{self._dmg} TTK:{self._ttk}"

    def target(self,beam_damage):
        damage_dealt = beam_damage
        if self._type == "FIGHTER":
            damage_dealt *= 2 
        damage_dealt -= self._armor
        if damage_dealt < 1:
            damage_dealt = 1
        return damage_dealt

    def get_hit(self,damage_dealt):
        self._hp -= damage_dealt

    def ttk(self,beam_damage):
        self._ttk = math.ceil(self._hp/self.target(beam_damage))

BEAM_DAMAGE = 10
SHIELD = 5000

n = int(input())

ships = []
for i in range(n):
    _type, hp, armor, damage = input().split()
    hp = int(hp)
    armor = int(armor)
    damage = int(damage)
    ships.append(Ship(_type,hp,armor,damage))


for ship in ships:
    ship.ttk(BEAM_DAMAGE)

res = solve(ships,BEAM_DAMAGE,SHIELD)

print(res)
