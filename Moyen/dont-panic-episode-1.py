import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

def goodDir(clone_pos,exit_pos,direction):
    if direction == "RIGHT":
        return True if exit_pos - clone_pos >= 0 else False
    else:
        return True if clone_pos - exit_pos >= 0 else False
        

# nb_floors: number of floors
# width: width of the area
# nb_rounds: maximum number of rounds
# exit_floor: floor on which the exit is found
# exit_pos: position of the exit on its floor
# nb_total_clones: number of generated clones
# nb_additional_elevators: ignore (always zero)
# nb_elevators: number of elevators
nb_floors, width, nb_rounds, exit_floor, exit_pos, nb_total_clones, nb_additional_elevators, nb_elevators = [int(i) for i in input().split()]
elevator_Dic = {}
for i in range(nb_elevators):
    # elevator_floor: floor on which this elevator is found
    # elevator_pos: position of the elevator on its floor
    elevator_floor, elevator_pos = [int(j) for j in input().split()]
    elevator_Dic[elevator_floor] = elevator_pos

print(elevator_Dic,file=sys.stderr)
# game loop
last_block = -1
while True:
    # clone_floor: floor of the leading clone
    # clone_pos: position of the leading clone on its floor
    # direction: direction of the leading clone: LEFT or RIGHT
    clone_floor, clone_pos, direction = input().split()
    clone_floor = int(clone_floor)
    clone_pos = int(clone_pos)
    print(clone_floor,clone_pos,direction,last_block,file=sys.stderr)

    if (clone_floor == -1 and clone_pos == -1 and direction == "NONE") or clone_floor == last_block:
        print("WAIT")
    elif clone_floor == exit_floor:
        if not goodDir(clone_pos,exit_pos,direction):
            print("BLOCK")
            last_block = clone_floor
        else:
            print("WAIT")
    else:
        if not goodDir(clone_pos,elevator_Dic[clone_floor],direction):
            print("BLOCK")
            last_block = clone_floor
        else:
            print("WAIT")

    
    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr)

    # action: WAIT or BLOCK
 