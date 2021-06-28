import random
from product import product
from jssp_instance import instance
from construct_heurstic import construct_sol
from solution import solution
from tryingstuff import *



def random_lot(sol_temp, j):
    passes = 0
    if j < sol_temp.inst.mfab:
        while (passes == 0): 
            l = random.choice(range(len(sol_temp.Y[0]))) # choisir un lot au hasarad et vérifier si il passe par la machine j
            if sum([sol_temp.inst.fab[i][j] * sol_temp.inst.b[i][l] for i in range(sol_temp.inst.n)]) == 1:
                passes =1
                return l
    else:
        while (passes == 0): 
            l = random.choice(range(len(sol_temp.Y[0]))) # choisir un lot au hasarad et vérifier si il passe par la machine j
            if sol_temp.X[l][j-sol_temp.inst.mfab] == 1:
                passes =1
                return l

def check_process(sol_temp, l, j):
    mfab = sol_temp.inst.mfab
    if j < mfab:
        k = int(sum([sol_temp.inst.fab[i][j] * sol_temp.inst.b[i][l] for i in range(sol_temp.inst.n)]))
        return k
    else:
        return sol_temp.X[l][j-mfab]

def getlot_before(sol_temp, l,j, somme_Y):
    pos_l2 = somme_Y[l] +1
    ind_l2 = somme_Y.index(pos_l2)
    while check_process(sol_temp, ind_l2, j) == 0 & pos_l2 < len(somme_Y):
        pos_l2 += 1
        ind_l2 = somme_Y.index(pos_l2)
    return ind_l2

def getlot_after(sol_temp, l, j, somme_Y):
    pos_l2 = somme_Y[l] - 1
    ind_l2 = somme_Y.index(pos_l2)
    while (check_process(sol_temp, ind_l2, j) == 0) & (pos_l2 > 0):
        pos_l2 -= 1
        ind_l2 = somme_Y.index(pos_l2)
    return ind_l2

class tabu_searhc:
    def __init__(self, sol_init, n_max,iter_max):
        self.sol_init = sol_init
        self.n_max = n_max
        self.iter_max = iter_max

    def Y_move(self, sol_temp):
        print("on va changer sur Y")
        j = random.choice(range(sol_temp.inst.mfab)) # choix aléatoire de la machine 
        print("on a choisit la machine", j)
        somme_Y = [sum(sol_temp.Y[j][l]) for l in range(len(sol_temp.Y[0]))]
        l = random_lot(sol_temp, j)
        print("on a choisit le lot", l)
        bef_aft = random.choice([1,2])
        print("bef_aft =", bef_aft)
        print('somme_Y[l] = ', somme_Y[l])
        if ((bef_aft == 1) & (somme_Y[l]!=len(sol_temp.Y[0]) -1)) | (somme_Y[l] == 0) : # on permute avec le lot qui vient AVANT
            print(" on va partir vers le lot d'avant")
            ind_l2 = getlot_before(sol_temp, l, j, somme_Y)
            if (check_process(sol_temp, ind_l2, j) == 0 & somme_Y[ind_l2] == len(somme_Y)):
                ind_l2 = getlot_after(sol_temp, l, j, somme_Y) ## problem if the lot is the only one procesed on j 
            sol_temp.Y[j][l][ind_l2],sol_temp.Y[j][ind_l2][l] = sol_temp.Y[j][ind_l2][l],sol_temp.Y[j][l][ind_l2]
        else:
            print(" on va partir vers le lot d'après")
            ind_l2 = getlot_after(sol_temp, l, j, somme_Y)
            if (check_process(sol_temp, ind_l2, j) == 0 & somme_Y[ind_l2] == len(somme_Y)):
                ind_l2 = getlot_before(sol_temp, l, j, somme_Y) ## problem if the lot is the only one procesed on j 
            sol_temp.Y[j][l][ind_l2],sol_temp.Y[j][ind_l2][l] = sol_temp.Y[j][ind_l2][l],sol_temp.Y[j][l][ind_l2]
                
    def U_move(self, sol_temp):
        print("on a changer sur U")
        a = random.choice(range(sol_temp.inst.lin)) # choix aléatoire de la ligne 
        print("on a choisit la ligne", a)
        somme_U = [sum(sol_temp.U[a][l]) for l in range(len(sol_temp.U[0]))]
        l = random_lot(sol_temp, a)
        print("on a choisit le lot", l)
        bef_aft = random.choice([1,2])
        print("on a choisit d'aller", bef_aft)
        print("somme_U[l] = ", somme_U[l])
        if ((bef_aft == 1) & (somme_U[l]!= len(sol_temp.U[0]) -1)) | (somme_U[l] == 0) : # on permute avec le lot qui vient AVANT
            print(" on va partir vers le lot d'avant")
            ind_l2 = getlot_before(sol_temp, l, a, somme_U)
            if (check_process(sol_temp, ind_l2, a) == 0 & somme_U[ind_l2] == len(somme_U)):
                ind_l2 = getlot_after(sol_temp, l, a, somme_U) ## problem if the lot is the only one procesed on j 
            sol_temp.U[a][l][ind_l2],sol_temp.U[a][ind_l2][l] = sol_temp.U[a][ind_l2][l],sol_temp.U[a][l][ind_l2]
        else:
            print(" on va partir vers le lot d'après")
            ind_l2 = getlot_after(sol_temp, l, a, somme_U)
            if (check_process(sol_temp, ind_l2, a) == 0 & somme_U[ind_l2] == len(somme_U)):
                ind_l2 = getlot_before(sol_temp, l, a, somme_U) ## problem if the lot is the only one procesed on j 
            sol_temp.U[a][l][ind_l2],sol_temp.U[a][ind_l2][l] = sol_temp.U[a][ind_l2][l],sol_temp.U[a][l][ind_l2]

    def X_move(self, sol_temp):
        print("on va changer sur X")
        done= 0
        while done == 0:
            l = random.choice(range(sum(sol_temp.inst.lots)))
            print("le lot choisit est", l)
            a_actu = sol_temp.X[l].index(1)
            print("sa ligne actuelle est", a_actu)
            a = random.choice(range(sol_temp.inst.lin))
            print("la ligne choisit est", a)
            con_a=sum([sol_temp.inst.con[i][a] * sol_temp.inst.b[i][l] for i in range(sol_temp.inst.n)])
            print("est-ce que l peut passer par a", con_a==1)
            if (con_a == 1) & (a != a_actu) :
                print("I'll change it now")
                sol_temp.X[l][a_actu],sol_temp.X[l][a] = sol_temp.X[l][a],sol_temp.X[l][a_actu]
                done = 1
        
        
    
    def move(self,sol_temp ):
        k = random.choice([1, 2, 3]) # choix aléatoire de la mtrice à modifier 1-> Y, 2-> U, 3-> X
        #k=3
        if k == 1: 
            self.Y_move(sol_temp)
            #print("le nouveau Y", self.sol_init.Y)
        else: 
            if k == 2:
                self.U_move(sol_temp)
                #print("le nouveau U", self.sol_init.U)
            else:
                self.X_move(sol_temp)
                #print("le nouveau X", self.sol_init.X)
        #return movement


# example -----
tabu_sol = tabu_searhc(sol_init, 8,8)
#print ("Y = ", sol_init.Y)
#print ("U = ", sol_init.U)
#print ("X = ", sol_init.X)
#j = random.choice(range(mfab))
#l = random.choice(range(jssp.L))
#k = sum([sol_init.inst.fab[i][j] * sol_init.inst.b[i][l] for i in range(sol_init.inst.n)])
#print("k=", k)
print("Cmax initial =", sol_init.Cmax)

tabu_sol.move(sol_init)
sol = solution(jssp, sol_init.X, sol_init.Y, sol_init.U)
sol.decode()
print("did somethin change?", 
((sol_init.Y == sol_const.Y) & (sol_init.U == sol_const.U) & (sol_init.X == sol_const.X)) )
print("Cmax = ", sol.Cmax)
print("--- %s seconds to move and decode ---" % (time.time() - start_time))
"""
print(hex(id(sol_init.Y[0])))
print(hex(id(sol_init.Y[1])))
print(hex(id(sol_init.Y[2])))
                
"""


