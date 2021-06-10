import numpy as np

class instance :

    def __init__ (self, m, n, lin ,dem, sinit,sec):
        self.mach= m
        self.prod = n
        self.dem = dem
        self.sinit = sinit
        self.sec = sec
        self.times =[]
        self.lin = lin
        self.b=[]
        self.g = []
        self.fab=[]
        self.con=[]
        self.mfab= m-lin
        self.pc=[]

    def getpt(self):
        for i in range(self.prod):
            jtimes=[]
            for j in range (self.mach):
                print("Le temps de traitement de l'opération", j+1, "du produit ",i+1)
                t=input()
                jtimes.append(int(t))
            self.times.append(jtimes)
    
    def fillfab(self):
        for i in range(self.prod):
            jfab=[]
            for j in range(self.mfab):
                if self.times[i][j] != 0:
                    jfab.append(1) #if the product i is processed in the machine j
                else:
                    jfab.append(0) #if the product i skips the machine j
            self.fab.append(jfab)
        return self.fab 

        




def greedyjs(prob):
    ord=[]
    id=prob.pc.index(min(prob.pc))
    poslot=[]
    for j in range(prob.lin):
        prob.con[id][j]

"""


hydra=instance(3,2,2, 10, 1, 5)

mat = [10,20,3]
print(mat.index(min(mat)))