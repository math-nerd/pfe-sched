import random
from product import product
from jssp_instance import instance
from construct_heurstic import construct_sol
from solution import solution
import copy
#from random_sol import fill_X, fill_YU



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

def Y_move(sol):
    sol_temp = copy.deepcopy(sol)
    #j = random.choice(range(sol_temp.inst.mfab)) # choix aléatoire de la machine 
    somme_Y = [sum(sol_temp.Y[0][l]) for l in range(len(sol_temp.Y[0]))]
    #print("somm_Y=",  somme_Y)
    l = random_lot(sol_temp, 0)
    bef_aft = random.choice([1,2])
    if ((bef_aft == 1) & (somme_Y[l]!=len(sol_temp.Y[0]) -1)) | (somme_Y[l] == 0) : # on permute avec le lot qui vient AVANT
        ind_l2 = getlot_before(sol_temp, l, 0, somme_Y)
        if (check_process(sol_temp, ind_l2, 0) == 0 & somme_Y[ind_l2] == len(somme_Y)):
            ind_l2 = getlot_after(sol_temp, l, 0, somme_Y) ## problem if the lot is the only one procesed on j 
        sol_temp.Y[0][l][ind_l2],sol_temp.Y[0][ind_l2][l] = sol_temp.Y[0][ind_l2][l],sol_temp.Y[0][l][ind_l2]
    else:
        ind_l2 = getlot_after(sol_temp, l, 0, somme_Y)
        if (check_process(sol_temp, ind_l2, 0) == 0 & somme_Y[ind_l2] == len(somme_Y)):
            ind_l2 = getlot_before(sol_temp, l, 0, somme_Y) ## problem if the lot is the only one procesed on j 
        sol_temp.Y[0][l][ind_l2],sol_temp.Y[0][ind_l2][l] = sol_temp.Y[0][ind_l2][l],sol_temp.Y[0][l][ind_l2]
    
    for j in range(sol_temp.inst.mfab):
        sol_temp.Y[j] = copy.deepcopy(sol_temp.Y[0])
    for a in range(sol_temp.inst.lin):
        sol_temp.U[a] = copy.deepcopy(sol_temp.Y[0])

    return [sol_temp, ("Y/U",l,ind_l2)]
"""           
def U_move(sol_temp):
    a = random.choice(range(sol_temp.inst.lin)) # choix aléatoire de la ligne 
    somme_U = [sum(sol_temp.U[a][l]) for l in range(len(sol_temp.U[0]))]
    print("somm_U= ", somme_U)
    l = random_lot(sol_temp, a)
    bef_aft = random.choice([1,2])
    if ((bef_aft == 1) & (somme_U[l]!= len(sol_temp.U[0]) -1)) | (somme_U[l] == 0) : # on permute avec le lot qui vient AVANT
        ind_l2 = getlot_before(sol_temp, l, a, somme_U)
        if (check_process(sol_temp, ind_l2, a) == 0 & somme_U[ind_l2] == len(somme_U)):
            ind_l2 = getlot_after(sol_temp, l, a, somme_U) ## problem if the lot is the only one procesed on j 
        sol_temp.U[a][l][ind_l2],sol_temp.U[a][ind_l2][l] = sol_temp.U[a][ind_l2][l],sol_temp.U[a][l][ind_l2]
    else:
        ind_l2 = getlot_after(sol_temp, l, a, somme_U)
        if (check_process(sol_temp, ind_l2, a) == 0 & somme_U[ind_l2] == len(somme_U)):
            ind_l2 = getlot_before(sol_temp, l, a, somme_U) ## problem if the lot is the only one procesed on j 
        sol_temp.U[a][l][ind_l2],sol_temp.U[a][ind_l2][l] = sol_temp.U[a][ind_l2][l],sol_temp.U[a][l][ind_l2]

    return [sol_temp, ("U", a,l,ind_l2)]
"""

def X_move(sol):
    sol_temp = copy.deepcopy(sol)

    done= 0
    while done == 0:
        l = random.choice(range(sum(sol_temp.inst.lots)))
        a_actu = sol_temp.X[l].index(1)
        a = random.choice(range(sol_temp.inst.lin))
        con_a=sum([sol_temp.inst.con[i][a] * sol_temp.inst.b[i][l] for i in range(sol_temp.inst.n)])
        if (con_a == 1) & (a != a_actu) :
            sol_temp.X[l][a_actu],sol_temp.X[l][a] = sol_temp.X[l][a],sol_temp.X[l][a_actu]
            done = 1
    
    return [sol_temp, (l, a_actu,a)]

def move(sol):
    sol_temp = copy.deepcopy(sol)
    #k = random.choice([1, 2, 3]) # choix aléatoire de la mtrice à modifier 1-> Y, 2-> U, 3-> X
    k = random.choice([1, 2,3]) 
    if k == 1: 
        the_move = Y_move(sol_temp)
        the_move[0].FT = []
        the_move[0].CT = [0]*sum(the_move[0].inst.lots)
        the_move[0].Cmax = 0
        #print("le nouveau Y", the_move[0].Y)
    else: 
        if k == 2:
            the_move = Y_move(sol_temp)
            the_move[0].FT = []
            the_move[0].CT = [0]*sum(the_move[0].inst.lots)
            the_move[0].Cmax = 0

            #print("le nouveau U", the_move[0].U)
        else:
            #print("we change X")
            the_move = X_move(sol_temp)
            the_move[0].FT = []
            the_move[0].CT = [0]*sum(the_move[0].inst.lots)
            the_move[0].Cmax = 0
            #print("le nouveau X", the_move[0].X)
    return the_move


