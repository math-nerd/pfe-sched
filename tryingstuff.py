import math
from tabu_new import tabu_serach
import time
from product import product
from jssp_instance import instance
from solution import solution
from construct_heurstic import construct_sol
from move_sol import move
from gantt import *





def colonne(liste, j): ## fonction pour avoir la colonne j+1 d'une matrice (liste de listes)
    return[item[j] for item in liste]

start_time = time.time()
mfab=3
lin=2
netmin = [0.5, 1]
netmaj = [4, 16]
#on définit les produit
prod1 = product('produit1', [3, 5, 3, 16, 0], 16, 2, 0, 0,1)
prod2 = product('produit2', [3, 5, 3, 21, 0], 21, 3, 0, 0, 1)
prod3 = product('produit3', [3, 5, 3, 22, 22], 22, 2, 0, 0, 1)
prod4 = product('produit4', [3, 5, 3, 0, 15], 15, 1, 0, 0, 1)
prod5 = product('produit5', [3, 5, 3, 0, 24], 24, 46, 0, 0, 23)
prod6 = product('produit1', [3, 5, 3, 16, 0], 16,46, 0, 0, 46)
prod=[prod1, prod2, prod3, prod4, prod5, prod6]
jssp = instance(mfab, lin , netmin, netmaj, prod)
jssp.process_input()

sol_const= construct_sol(jssp)
sol_const.greedy()

sol =solution(jssp, sol_const.X, sol_const.Y, sol_const.U)
sol.decode()
print("Y =", sol.Y)
print("U =", sol.U)
print("X =", sol.X)
print("FT =", sol.FT)
print("CT = ", sol.CT)
print("Cmax =", sol.Cmax)

sol_fin = tabu_serach(sol, 10, 100)
gantt_chart(sol_fin, "Juillet")
"""
neighbor = move(sol)
sol_nei = neighbor[0]
movement = neighbor[1]
print("mouvement", movement)
print("new FT", sol_nei.FT)
print("new CT", sol_nei.CT)
print("new Cmax", sol_nei.Cmax)
sol_nei.decode()
print("new new FT", sol_nei.FT)
print("new new CT", sol_nei.CT)
print("new new Cmax", sol_nei.Cmax)

print("--- %s seconds to construct the solution ---" % (time.time() - start_time))
"""