import copy
from data import *
from construct_heurstic import construct_sol
from solution import solution
from tabu_new import tabu_serach
from SA import simulated_annealing
from gantt import *

def plan(i,j): 
    start_time = time.time()
    for month in range (i,j+1):
        jssp_pb = copy.deepcopy(jssp[month])
        #construire la solution intiale 
        sol_const = construct_sol(jssp_pb)
        sol_const.greedy()
        X= sol_const.X
        Y= sol_const.Y
        U= sol_const.U
        sol_init = solution(jssp_pb, X, Y, U)
        sol_init.decode()
        """
        print("FT = ", sol_init.FT)
        print("CT = ", sol_init.CT)
        print("Cmax = ", sol_init.Cmax)
        """
        # commencer la métaheuristiques
        sol_fin = tabu_serach(sol_init, 10, 10)
        
        #print("We found the solution")
        #print('X = ', sol_fin.X)
        FT = sol_fin.FT
        #print("FT = ", FT)
        CT = sol_fin.CT
        #print("CT = ", CT)
        Cmax = sol_fin.Cmax
        #print("Cmax = ", Cmax)
        gantt_chart(sol_fin, month)
        print("--- %s seconds to finish it all ---" % (time.time() - start_time))




    
