import random
import copy
from product import product
from jssp_instance import instance
from solution import solution

def get_prod_before(p, order_p, indice_p):
    p2_pos = order_p[p] - 1
    p2_indice = order_p.index(p2_pos) # indice du produit traité avant
    p2_lot_index = indice_p[p2_indice] #indice du premier lot du produit traité avant
    return p2_indice, p2_lot_index

def get_prod_after(p, order_p, indice_p):
    p2_pos = order_p[p] + 1
    p2_indice = order_p.index(p2_pos) # indice du produit traité avant
    p2_lot_index = indice_p[p2_indice] #indice du premier lot du produit traité avant
    return p2_indice, p2_lot_index

def move_YU(sol):
    p = random.choice(range(sol.inst.n)) # we choose the product at random
    indice_p = [0]
    for l in range(sol.inst.n-1):
        indice_p.append(indice_p[l]+sol.inst.lots[l])
    somme_Y = [sum(sol.Y[0][l]) for l in indice_p]
    order_p = [0]*sol.inst.n
    for i in range(sol.inst.n):
        l = somme_Y.index(max(somme_Y))
        order_p[l] = i
        somme_Y[l] = -1
    p_lot= indice_p[p]
    bef_aft=random.choice([1,2])
    if ((bef_aft == 1) & (order_p[p] != 0)) | (order_p[p] == sol.inst.n - 1): # we choose the the product before
        p2, p2_lot = get_prod_before(p, order_p,indice_p)
        for l in range(p_lot, p_lot+sol.inst.lots[p]):
            for k in range(p2_lot, p2_lot+sol.inst.lots[p2]):
                sol.Y[0][l][k],sol.Y[0][k][l] =sol.Y[0][k][l],sol.Y[0][l][k]
    else:
        p2, p2_lot = get_prod_after(p, order_p, indice_p)
        for l in range(p_lot, p_lot+sol.inst.lots[p]):
            for k in range(p2_lot, p2_lot+sol.inst.lots[p2]):
                sol.Y[0][l][k],sol.Y[0][k][l] =sol.Y[0][k][l],sol.Y[0][l][k]
    for j in range(sol.inst.mfab):
        sol.Y[j] = copy.deepcopy(sol.Y[0])
    for a in range(sol.inst.lin):
        sol.U[a] = copy.deepcopy(sol.Y[0])
    return [sol, ("Y/U",p,p2)]

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
    



def move_prod(sol):
    k = random.choice([1,2,3])
    if k != 3:
        nei = move_YU(sol)
    else:
        nei = X_move(sol)
    nei[0].FT = []
    nei[0].CT = [0]*sum(sol.inst.lots)
    nei[0].Cmax = 0
    nei[0].finfab=[]
    nei[0].fincon=[]

    return nei
    
