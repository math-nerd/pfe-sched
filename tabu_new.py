import time
import copy
from math import sqrt
from product import product
from jssp_instance import instance
from solution import solution
from construct_heurstic import construct_sol
#from move_sol import *
from move_sol2 import *
start_time = time.time()

def update_TL(TL, move):
    rev_move = (move[0], move[2], move[1])
    TL.insert(0, rev_move)
    TL.pop()



def tabu_serach(sol_i, n_max, iter_max):
    sol_temp = copy.deepcopy(sol_i)
    sol_best = copy.deepcopy(sol_i)
    TL_size = int(sqrt(sol_i.inst.L*sol_i.inst.m))
    #print("TL size =", TL_size)
    TL = [0]*TL_size
    #print("TL =", TL)
    it = 0
    sol_temp.decode()
    sol_best.decode()
    obj1 = sol_temp.Cmax
    #print("Cmax initial= ", obj1)
    obj_best = sol_temp.Cmax
    while (it < iter_max):
        L =[]
        n_size = 0 
        #print("la taille de voisinnage commence de", n_size)
        found = 0
        obj_nei_best = 1000000000000000000000
        while ((n_size < n_max) & (found == 0)):
            neighboor = copy.deepcopy(move_prod(sol_temp))
            tal = copy.deepcopy(neighboor[1])
            while (tal in L):
                neighboor = copy.deepcopy(move_prod(sol_temp))
                tal = copy.deepcopy(neighboor[1])
            L.append(tal)
            sol_nei = copy.deepcopy(neighboor[0])
            #print("tal =", tal)
            sol_nei.decode()
            obj_nei = sol_nei.Cmax
            #print("we have a solution", obj_nei)
            if (obj_nei < obj_nei_best):
                #print("this solution is the new best in the neigberhood", obj_nei)
                obj_nei_best = obj_nei
                sol_nei_best = copy.deepcopy(sol_nei)
                tal_nei_best = copy.deepcopy(tal)
            if (tal not in TL):
                #print("solution not tabu")
                if (obj_nei < obj1):
                    #print("solution better than current solution")
                    sol_temp = copy.deepcopy(sol_nei)
                    obj1 = obj_nei
                    found = 1
                    update_TL(TL, tal)
                    #print('TL =', TL)
                    if (obj_nei < obj_best):
                        #print("solution best ever")
                        sol_best = copy.deepcopy(sol_nei)
                        obj_best = obj_nei
                        it = 0
                    else:
                        it += 1
                        #print("on est à l'itération", it)
                else:
                    #print("solution worse than current solution")
                    n_size +=1
                    #print("la taille du voisinnage augmente", n_size)
            else:
                #print("solution tabou")
                if (obj_nei < obj_best): 
                    sol_temp = copy.deepcopy(sol_nei)
                    obj1 = obj_nei
                    sol_best = copy.deepcopy(sol_nei)
                    obj_best = obj_nei
                    it = 0
                    found = 1
                    #print("critère d'asspiration satisfait", )
                    update_TL(TL, tal)
                else:
                    n_size +=1
        if (n_size == n_max):
            #print(" we didn't find a good solution")
            sol_temp = copy.deepcopy(sol_nei_best)
            obj1 = obj_nei
            #print("we too the sol", obj1)
            it += 1
            update_TL(TL, tal_nei_best)
        
    return sol_best
"""
#Let's try
mfab=3
lin=2
netmin = 1
netmaj = 16
#on définit les produit

prod1 = product('produit1', [3, 5, 3, 16, 0], 16, 1, 0, 0,1)
prod2 = product('produit2', [3, 5, 3, 21, 0], 21, 1, 0, 0, 1)
prod3 = product('produit3', [3, 5, 3, 22, 22], 22, 1, 0, 0, 1)
prod4 = product('produit4', [3, 5, 3, 0, 15], 15, 1, 0, 0, 1)
prod5 = product('produit5', [3, 5, 3, 0, 24], 24, 1, 0, 0, 1)
prod6 = product('produit1', [3, 5, 3, 16, 0], 16,1, 0, 0, 1)

prod6 = product('produit1', [3, 5, 3, 16, 0], 16, 20, 0, 0,1)
prod4 = product('produit2', [3, 5, 3, 21, 0], 21, 5, 0, 0, 1)
prod2 = product('produit3', [3, 5, 3, 22, 22], 22, 16, 0, 0, 1)
prod3 = product('produit4', [3, 5, 3, 0, 15], 15, 10, 0, 0, 1)
prod1 = product('produit5', [3, 5, 3, 0, 24], 24, 2, 0, 0, 1)
prod5 = product('produit1', [3, 5, 3, 16, 0], 16,6, 0, 0, 1)

prod=[prod1, prod2, prod3, prod4, prod5, prod6]

jssp = instance(mfab, lin , netmin, netmaj, prod)
jssp.process_input()
#print("--- %s seconds to process the input ---" % (time.time() - start_time))
#start_time = time.time()
sol_const = construct_sol(jssp)
sol_const.greedy()
#print("--- %s seconds to construct solution ---" % (time.time() - start_time))



Y = sol_const.Y
U = sol_const.U 
X = sol_const.X
#print("this works")
#print("X", X)
sol_const = solution(jssp, X, Y, U)
sol_const.decode()
#print('FT = ', sol_const.FT)
#print('CT = ', sol_const.CT)
#print('Cmax = ', sol_const.Cmax)
#print("Y initial", Y)
#print("Y initial", U)
#print("Y initial", X)
#sol_init = solution(jssp, X, Y, U)
#sol_init.decode()
#print('Cmax = ', sol_init.Cmax)
sol = tabu_serach(sol_const, 10, 100)
print('Cmax =', sol.Cmax)
print('FT = ', sol.FT)
print('CT = ', sol.CT)
print("Y =", sol.Y)
print("U = ", sol.U)
print('X = ', sol.X)
#print("--- %s seconds to tabu search---" % (time.time() - start_time))
"""