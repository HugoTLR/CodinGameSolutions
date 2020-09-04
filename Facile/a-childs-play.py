import sys
import math
import time


directions = [(-1,0),(0,1),(1,0),(0,-1)]


def play(memo,board,moves,robot_pos,width):
    start = time.time()
    
    dir_ind = 0
    initial_dir = dir_ind
    initial_pos = robot_pos
    initial_cell_id = initial_pos[0]*width+initial_pos[1]
    done_moves = 0
    
    
    memo[initial_cell_id][dir_ind]
    
    while moves > 0:
        direction = directions[dir_ind]
        cell_id = robot_pos[0]*width+robot_pos[1]
        if memo[cell_id][dir_ind] != None:
            print("We made a full loop!, exiting algorithm...",file=sys.stderr)
            full_loop_remaining = moves//(done_moves)#Trickster
            extra_move_remaining = moves%(done_moves)

            for _ in range(extra_move_remaining):
                robot_pos = memo[cell_id][dir_ind][0]
                dir_ind = memo[cell_id][dir_ind][1]
                cell_id = robot_pos[0]*width+robot_pos[1]
                
            moves = 0
            
        else:
            new_robot_pos = (robot_pos[0]+direction[0],robot_pos[1]+direction[1])

            if board[new_robot_pos[0]][new_robot_pos[1]] == '#':

                tmp = dir_ind
                dir_ind =  (dir_ind + 1)%4
                if robot_pos == initial_pos and dir_ind == initial_dir:
                    continue
                new_direction = directions[dir_ind]
                new_robot_pos = (robot_pos[0]+new_direction[0],robot_pos[1]+new_direction[1])
                
                memo[cell_id][tmp] = (new_robot_pos,dir_ind)
            else:
                memo[cell_id][dir_ind] = (new_robot_pos,dir_ind)
            
            robot_pos = new_robot_pos
            moves -= 1
            done_moves += 1
            
    
    print(f"Computed 'play' method in {time.time()-start:5f} secs" ,file=sys.stderr)
    return robot_pos,memo
    
    
#Input sequences    
w, h = [int(i) for i in input().split()]
n = int(input())
board = []
# Memo array
# 2D array H= w*h (number of cells), W=4 (number of dir)
# Can be improved deleting rows of # block as we can't walk on it, but FLEMME
# for a cell of the array, contain a tuple ( new_pos, direction Index) to update direction on memo
memo = [[None]*4 for _ in range(w*h)]


robotFound = False
robot_pos = (0,0)
for j in range(h):
    board.append([c for c in input()])
    if not robotFound:
        i = 0
        for c in board[-1]:
            if c == 'O':
                
                robot_pos = (j,i)
                robotFound = True
                
            i += 1
board[robot_pos[0]][robot_pos[1]] = '.' # Remove robot for algo   

robot_pos,memo = play(memo,board,n,robot_pos,w) 
"""
for row in memo:
    print(row,file=sys.stderr)
"""

print(f"{robot_pos[1]} {robot_pos[0]}") 

