import sys
import math
from functools import cmp_to_key

class Robot:
    def __init__(self):
        self.target = None
        self.score = 0
        self.current_molecules = {"A":0, "B":0, "C":0, "D":0, "E":0}
                                    
    def __str__(self):
        res = f"Target:{self.target} Score:{self.score}\n"
        for mol in self.current_molecules.keys():
            res = res + f"\t{mol}: {self.current_molecules[mol]}\n"
        return res
    def update(self,**kwargs):
        self.score = kwargs['score']
        self.target = kwargs['target']
        for k in self.current_molecules.keys():
            self.current_molecules[k] = kwargs[k]
    
    def has_enough_molecules(self,f):
        return self.current_molecules["A"] >= f["costA"] and \
                self.current_molecules["B"] >= f["costB"] and \
                self.current_molecules["C"] >= f["costC"] and \
                self.current_molecules["D"] >= f["costD"] and \
                self.current_molecules["E"] >= f["costE"]
    
    def select_molecule(self,f):
        if self.current_molecules["A"] < f["costA"]:
            return "A"
        elif self.current_molecules["B"] < f["costB"]:
            return "B"
        elif self.current_molecules["C"] < f["costC"]:
            return "C"
        elif self.current_molecules["D"] < f["costD"]:
            return "D"
        else:
            return "E"

def custom_sort(f1,f2):
    f1_mol = f1['A'] + f1['B'] + f1['C'] + f1['D'] + f1['E'] 
    f2_mol = f2['A'] + f2['B'] + f2['C'] + f2['D'] + f2['E'] 
    if f1_mol > f2_mol:
        return 1
    elif f1_mol == f2_mol:
        return 0
    else:
        return -1

def get_best_file(files_dic):
    avaiable_files = [f for f in files_dic.values() if f['carried_by'] == -1]
    avaiable_files = sorted(avaiable_files,key=lambda x: x['total_cost'])
    return avaiable_files[0]


def is_diag(f):
    return f['health'] > 0

# Bring data on patient samples from the diagnosis machine to the laboratory with enough molecules to produce medicine!

project_count = int(input())
for i in range(project_count):
    a, b, c, d, e = [int(j) for j in input().split()]

my_robot = Robot()
opp_robot = Robot()



# game loop
while True:
    print(f"\n----- ROBOT -----",file=sys.stderr)
    
    files_dic = {}
    for i in range(2):
        target, eta, score, storage_a, storage_b, storage_c, storage_d, storage_e, expertise_a, expertise_b, expertise_c, expertise_d, expertise_e = input().split()
        eta = int(eta)
        score = int(score)
        storage_a = int(storage_a)
        storage_b = int(storage_b)
        storage_c = int(storage_c)
        storage_d = int(storage_d)
        storage_e = int(storage_e)

        if i == 0:
            my_robot.update(target=target, score=score, A=storage_a, \
                            B=storage_b, C=storage_c, D=storage_d, E=storage_e)
            print(str(my_robot),file=sys.stderr)
        else:
            opp_robot.update(target=target, score=score, A=storage_a, \
                            B=storage_b, C=storage_c, D=storage_d, E=storage_e)
            print(str(opp_robot),file=sys.stderr)



        expertise_a = int(expertise_a)
        expertise_b = int(expertise_b)
        expertise_c = int(expertise_c)
        expertise_d = int(expertise_d)
        expertise_e = int(expertise_e)
    available_a, available_b, available_c, available_d, available_e = [int(i) for i in input().split()]
    sample_count = int(input())
    for i in range(sample_count):
        sample_id, carried_by, rank, expertise_gain, health, cost_a, cost_b, cost_c, cost_d, cost_e = input().split()
        sample_id = int(sample_id)
        carried_by = int(carried_by)
        rank = int(rank)
        health = int(health)
        cost_a = int(cost_a)
        cost_b = int(cost_b)
        cost_c = int(cost_c)
        cost_d = int(cost_d)
        cost_e = int(cost_e)

        files_dic[sample_id] = {"id": sample_id, \
                                "carried_by": carried_by, \
                                "health": health, \
                                "rank": rank, \
                                "costA": cost_a, \
                                "costB": cost_b, \
                                "costC": cost_c, \
                                "costD": cost_d, \
                                "costE": cost_e, \
                                "total_cost": cost_a + cost_b + cost_c + cost_d + cost_e }
    
    print(f"----- FILES -----",file=sys.stderr)

    for k,v in files_dic.items():
        print(f"{k}: {v}",file=sys.stderr)



    my_files = [f for f in files_dic.values() if f['carried_by'] == 0]
    
    print(f"I got {len(my_files)} files",file=sys.stderr)
    for f in my_files:
        print(f"{f}",file=sys.stderr)
    
    #WHAT TO DO
    if len(my_files) == 0:
        if my_robot.target != "SAMPLES":
            print("GOTO SAMPLES")
        else:
            rank = 1
            print(f"CONNECT {rank}")
    else:
        my_file = my_files[0] #I suppose we onlyy grab one at once ?
        if not is_diag(my_file):
            if my_robot.target != "DIAGNOSIS":
                print("GOTO DIAGNOSIS")
            else:
                print(f"CONNECT {my_file['id']}")
        else:
            if not my_robot.has_enough_molecules(my_file):
                if my_robot.target != "MOLECULES":
                    print("GOTO MOLECULES")
                else:
                    #GRAB A NEEDED MOLECULE
                    molecule = my_robot.select_molecule(my_file)
                    print(f"CONNECT {molecule}")
            else:
                if my_robot.target != "LABORATORY":
                    print("GOTO LABORATORY")
                else:
                    #BUILD
                    print(f"CONNECT {my_file['id']}")


        

