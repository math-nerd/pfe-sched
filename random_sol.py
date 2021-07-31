import copy
from math import sqrt
from product import product
from jssp_instance import instance
from solution import solution
import random
from tabu_new import tabu_serach
from move_sol import *

def fill_YU(inst):
    Y = [[[0]*inst.L for _ in range(inst.L)] for _ in range(inst.mfab)]
    U = [[[0]*inst.L for _ in range(inst.L)] for _ in range(inst.lin)]
    somme =[i for i in range(inst.L)]
    random.shuffle(somme)
    
    for l in range(inst.L):
        s=somme[l]
        for k in range(inst.L):
            if somme[k] < somme[l]:
                Y[0][l][k]= 1
    for j in range(inst.mfab):
        Y[j]= copy.deepcopy(Y[0])
    for a in range(inst.lin):
        U[a]=copy.deepcopy(Y[0])
    return Y, U

def fill_X(inst):
    X = [[0]*inst.lin for _ in range(inst.L)]
    for l in range(inst.L):
        Lines = [i for i in range(inst.lin)]
        a = random.choice([i for i in Lines])
        k = sum([inst.con[i][a]* inst.b[i][l] for i in range(inst.n)])
          #=sum([self.inst.times[k][j] * self.inst.b[k][l] for k in range(self.inst.n)])
        while(k==0):
            Lines.remove(a)
            a = random.choice([i for i in Lines])
            k = sum([inst.con[i][a]* inst.b[i][l] for i in range(inst.n)])
        X[l][a] = 1
    return X            
        
mfab=3
lin=2
netmin = 1
netmaj = 16
#on définit les produit

prod1 = product('produit1', [3, 5, 3, 16, 0], 16, 1, 0, 0,1)
prod2 = product('produit2', [3, 5, 3, 0, 21], 21, 1, 0, 0, 1)
prod3 = product('produit3', [3, 5, 3, 22, 0], 22, 1, 0, 0, 1) #not like this 2 lines
#prod4 = product('produit4', [3, 5, 3, 0, 15], 15, 1, 0, 0, 1)
#prod5 = product('produit5', [3, 5, 3, 0, 24], 24, 23, 0, 0, 23)
#prod6 = product('produit1', [3, 5, 3, 16, 0], 16,46, 0, 0, 46)

prod=[prod1, prod2, prod3]#, prod4, prod5, prod6

jssp = instance(mfab, lin , netmin, netmaj, prod)
jssp.process_input()
"""
Y, U = fill_YU(jssp)
X = fill_X(jssp)
print("Y = ", Y)
print("U = ", U)
print("X = ", X)

sol = solution(jssp, X, Y, U)
sol.decode()
print("FT initial =", sol.FT)
print("CT initial =", sol.CT)
print('Cmax initial =', sol.Cmax)
"""
X = [[1, 0], [0, 1], [0, 1]]
Y = [[[0, 1, 1], [0, 0, 1], [0, 0, 0]], [[0, 1, 1], [0, 0, 1], [0, 0, 0]], [[0, 1, 1], [0, 0, 1], [0, 0, 0]]]
U = [[[0, 1, 1], [0, 0, 1], [0, 0, 0]], [[0, 1, 1], [0, 0, 1], [0, 0, 0]]]
sol2 = solution(jssp, X, Y, U)
sol2.decode()
print("new FT =", sol2.FT)
print("new CT =", sol2.CT)
print("New Cmax =", sol2.Cmax)
sol1 = move(sol2)[0]
print("new X =", sol1.X)
print("new Y =", sol1.Y)
print("new U =", sol1.U)
sol1.decode()
print("new FT =", sol1.FT)
print("new CT =", sol1.CT)
print("New Cmax =", sol1.Cmax)
sol_t = tabu_serach(sol2, 1, 50)
print(sol_t.Cmax)