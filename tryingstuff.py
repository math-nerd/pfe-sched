import math
import time
from product import product
from jssp_instance import instance
from solution import solution
from construct_heurstic import construct_sol

def colonne(liste, j): ## fonction pour avoir la colonne j+1 d'une matrice (liste de listes)
    return[item[j] for item in liste]

start_time = time.time()

# Exemple de l'instance:
mfab=3
lin=2
netmin = 1
netmaj = 16
#on définit les produit
prod1 = product('produit1', [3, 5, 3, 16, 0], 16, 170, 0, 0,1)
prod2 = product('produit2', [3, 5, 3, 21, 0], 21, 15, 0, 0, 1)
prod3 = product('produit3', [3, 5, 3, 22, 22], 22, 78, 0, 0, 4)
prod4 = product('produit4', [3, 5, 3, 0, 15], 15, 230, 0, 0, 1)
prod5 = product('produit5', [3, 5, 3, 0, 24], 24, 23, 0, 0, 1)
prod6 = product('produit1', [3, 5, 3, 16, 0], 16, 46, 0, 0, 1)
prod=[prod1, prod2, prod3, prod4, prod5, prod6]

# On définit l'instances
jssp = instance(mfab, lin , netmin, netmaj, prod)
# Là j'applique la méthode process_input fel main AVANT de déclarer l'objet sol_const and it works just fine
# But I don't want to do that x)
jssp.process_input()
print("--- %s seconds to process the input ---" % (time.time() - start_time))
sol_const = construct_sol(jssp)
sol_const.greedy()
print("--- %s seconds to construct the solution ---" % (time.time() - start_time))
# The rest works fine no need to take a look
Y = sol_const.Y
U = sol_const.U
X = sol_const.X

sol_init = solution(jssp, X, Y, U)
sol_init.decode()

print("Y = ", sol_init.Y)
print("U = ", sol_init.U)
print("X = ", sol_init.X)
print("FT =", sol_init.FT)
print("CT = ", sol_init.CT)
print("la valeur de la fonction objectif =", sol_init.Cmax)

print("--- %s seconds to decode ---" % (time.time() - start_time))