from product import product
import math

class instance : # classe des instances du problème
    def __init__ (self, mfab, lin , netmin, netmaj, prod):
        self.n = len(prod) #nombre de produit
        self.prod = prod #liste de produits
        self.lin = lin #nombre de lignes de conditionnement
        self.mfab= mfab # nombre de machine de fabrication
        self.netmin = netmin # temps de nettoyage mineur
        self.netmaj = netmaj # temps de nettoyage majeur
        self.times =[] # initialiser la matrice des temps de traitement
        self.b=[] # intialiser la matrice b (n*L) =1 si le lot l (colonne) est du produit i (lignes)
        self.g = [] # initialiser la matrice g (L*L) =1 si l et l' sont du même produit
        self.fab=[] # initialiser fab (n*mfab) = 1 si le produit i passe par la machine j
        self.con=[] # initialiser con (n*lin) = 1 si le produit i peut passer par la line a
        self.lots=[] # vecteur de nombre de lots à fabriquer pour chaque produit
        self.pc=[] # temps de conditionnement 
    
    def filllots(self):
        for i in range(self.n):
            self.lots.append(self.prod[i].lots)

    def filltimes(self):
        for i in range(self.n):
            self.times.append(self.prod[i].pt)
 
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
            for j in range(self.mfab,self.mfab+self.lin):
                if self.times[i][j] != 0:
                    jcon.append(1) #if the product i can be packaged on that line
                else:
                    jcon.append(0) #if the product i can't be packaged on that line
            self.con.append(jcon)
        return self.con 
    
    def fillb(self):
        r=0
        for i in range(self.n): 
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
        for i in range(self.n): 
            for l in range(r,r+self.lots[i]):
                self.g.append(self.b[i])
            r= r+self.lots[i]
        return self.g
    
    def fillpc (self):
        for i in range(self.n):
            self.pc.append(self.prod[i].pc)

    def process_input(self):
        self.filllots()
        self.filltimes()
        self.fillfab()
        self.fillcon()
        self.fillb()
        self.fillg()
        self.fillpc()



## Exemple
mfab=3
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

jssp = instance(mfab, lin , netmin, netmaj, prod)
jssp.process_input()
#print(jssp.fab)
#print(jssp.con)
#print(jssp.g)
#print(jssp.b)
#print(len(jssp.g))
