import copy
from product import product
from jssp_instance import instance
from solution import solution
from construct_heurstic import construct_sol
from move_sol import move
import random
import math

def simulated_annealing(sol_i):
    T = 10
    sol_temp = copy.deepcopy(sol_i)
    sol_best = copy.deepcopy(sol_i)
    T_fin = 0.5
    sol_temp.decode()
    sol_best.decode()
    obj1 = sol_temp.Cmax
    obj_best = sol_temp.Cmax
    alpha = 0.98
    iter_max = 1
    while (T >= T_fin):
        iter = 0
        while (iter < iter_max):
            neighboor = copy.deepcopy(move(sol_temp))
            sol_nei = copy.deepcopy(neighboor[0])
            sol_nei.decode()
            obj_nei = sol_nei.Cmax
            if (obj1 <= obj_nei):
                p = random.uniform(0, 1)
                if p <= math.exp((obj1-obj_nei)/T):
                    sol_temp = copy.deepcopy(sol_nei)
                    obj1 = obj_nei
            else:
                sol_temp = copy.deepcopy(sol_nei)
                obj1 = obj_nei
            if (obj_nei < obj_best):
                sol_best = copy.deepcopy(sol_nei)
                obj_best = obj_nei
            iter += 1
        T = T*alpha
    return sol_best

