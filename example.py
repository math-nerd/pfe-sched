from product import product
from jssp_instance import instance
from construct_heurstic import construct_sol
from solution import solution 
from tabu_new import tabu_serach
import time
start_time = time.time()
mfab = 3
n = 6
lin = 2
netmin = [0.5, 1]
netmaj = [4, 16]
jssp = []
prod1 = product("Produit1", [3, 5, 3, 32, 0], 32, 1, 14, 14, 1)
prod2 = product("Produit2", [3, 5, 3, 42, 0], 42, 1, 6, 6, 1 )
prod3 = product("Produit3", [3, 5, 3, 44, 44], 44, 1, 0, 0, 1)
prod4 = product("Produit4", [3, 5, 3, 0, 30], 30, 1, 0, 0, 1)
prod5 = product("Produit5", [3, 5, 3, 0, 48], 48, 1, 0, 0, 1)
prod6 = product("Produit6", [3, 5, 3, 32, 0], 32, 1, 0, 0, 1)
prod = [prod1, prod2, prod3, prod4,prod5,prod6]
jssp = instance(mfab, lin, netmin, netmaj, prod)
jssp.process_input()


print("b=", jssp.b)
print("g=", jssp.g)
print("fab=", jssp.fab)
print("con=", jssp.con)

sol_const = construct_sol(jssp)
sol_const.greedy()
X= sol_const.X
Y = sol_const.Y
U = sol_const.U
sol_init = solution(jssp, X, Y, U)
sol_init.decode()
#tabu search
sol_fin = tabu_serach(sol_init, 10, 1000)
print("Cmax", sol_fin.Cmax)
print()
print("--- La résolution est fait en: %s secondes ---" % (time.time() - start_time))