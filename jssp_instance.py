from product import product
import math
class instance :
    def __init__ (self, mfab, n, lin , netmin, netmaj, prod):
        self.n = n
        self.prod = prod
        self.lin = lin
        self.mfab= mfab
        netmin = netmin
        netmaj = netmaj
        self.times =[]
        self.b=[]
        self.g = []
        self.fab=[]
        self.con=[]
        self.lots=[]
        self.pc=[]

    def filltimes(self):
        for i in range(self.n):
            self.times.append(self.prod[i].times)
            """
            jtimes=[]
            for j in range (self.mach):
                print("Le temps de traitement de l'opération", j+1, "du produit ",i+1)
                t=input()
                jtimes.append(int(t))
            self.times.append(jtimes)
            self.lots.append(self.dem + int(self.sec) - int(self.sinit))
    """
    def fillfab(self):
        for i in range(self.n):
            jfab=[]
            for j in range(self.mfab):
                if self.times[i][j] != 0:
                    jfab.append(1) #if the product i is processed in the machine j
                else:
                    jfab.append(0) #if the product i skips the machine j
            self.fab.append(jfab)
        return self.fab 
    
    def fillcon(self):
        for i in range(self.n):
            jcon=[]
            for j in range(self.mfab,self.mach):
                if self.times[i][j] != 0:
                    jcon.append(1) #if the product i can be packaged on that line
                else:
                    jcon.append(0) #if the product i can't be packaged on that line
            self.cond.append(jcon)
        return self.cond 
    
    def fillb(self):
        r=0
        for i in range(self.prod): 
            lb=[]
            for l in range(sum(self.lots)):
                if (l>=r) & (l < r+self.lots[i]):
                    lb.append(1) #the batch l is of the product i
                else:
                    lb.append(0)
            self.b.append(lb)
            r=r+self.lots[i]
        return self.b  

    def fillg(self):
        r=0
        for i in range(self.prod): 
            for l in range(r,r+self.lots[i]):
                self.g.append(self.b[i])
            r= r+self.lots[i]
        return self.g

## Exemple
mfab=3
n=6
lin=2
netmin = 4
netmaj = 18
prod1 = product('produit1', [2, 3, 2, 18, 0], 18, 1000, 4, 5, 100)
prod2 = product('produit2', [1, 3, 3, 0, 16], 16, 2000, 5, 3, 150)
prod3 = product('produit3', [2, 4, 4, 20, 20], 20, 1500, 0, 5, 100)
prod4 = product('produit4', [3, 3, 0, 15, 15], 15, 1000, 0, 2, 175)
prod5 = product('produit5', [3, 2, 0, 18, 0], 18, 2550, 3, 10, 250)
prod6 = product('produit1', [2, 3, 0, 0, 17], 17, 3000, 7, 3, 200)

prod=[prod1, prod2, prod3, prod4, prod5, prod6]

jssp = instance(mfab, n, lin , netmin, netmaj, prod)
