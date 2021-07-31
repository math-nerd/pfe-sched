## fillfab-----------------------------------------------
class fonction:


    def fabfill(n,mfab,times):
        Fab=[]
        for i in range(n):
            jfab=[]
            for j in range(mfab):
                if times[i][j] != 0:
                    jfab.append(1) #if the product i is processed in the machine j
                else:
                    jfab.append(0) #if the product i skips the machine j
            Fab.append(jfab)
        return Fab
    

    def confill(n,m,times):
        Cond=[]
        for i in range(n):
            jcon=[]
            for j in range(mfab,m):
                if times[i][j] != 0:
                    jcon.append(1) #if the product i can be packaged on that line
                else:
                    jcon.append(0) #if the product i can't be packaged on that line
            Cond.append(jcon)
        return Cond
    
    def bfill(n,lots):
        b=[]
        r=0
        for i in range(n):
            lb=[]
            for l in range(sum(lots)):
                if (l>=r) & (l < r+lots[i]):
                    lb.append(1) #the batch l is of the product i
                else:
                    lb.append(0)
            b.append(lb)
            r=r+lots[i]
        return b 

## Algorithme de Salah-------------------------------------------
print("Résolution du problème F2//Cmax")
n=input("entrer le nombre de taches ")
n=int(n)
P1=[]
P2=[]
X=[]
X2=[]
tri=[]
machine1=[]
machine2=[]
print("entrer les temps de traitement")
for i in range(1,n+1):
    k=input(f"P1[{i}]=")
    k=int(k)
    k2=input(f"P2[{i}]=")
    k2=int(k2)
    P1.append(k)
    P2.append(k2)
    if(k<=k2):
        X.append(i)
    else:
        X2.append(i)

for i in range(len(X)):
    for j in range(i+1,len(X)):
        if(P1[X[i]-1]>P1[X[j]-1]):
            t=X[j]
            X[j]=X[i]
            X[i]=t

for i in range(len(X2)):
    for j in range(i+1,len(X2)):
        if(P2[X2[i]-1]<P2[X2[j]-1]):
            t=X2[j]
            X2[j]=X2[i]
            X2[i]=t
tri=X+X2
t=0
print("l'ordre des taches sur la première machine: ")
for i in range(len(tri)):
    machine1.append(t)
    tf=t+P1[tri[i]-1]
    print(f"t{tri[i]} :[{t},{tf}]")
    t=tf
    
t=P1[tri[0]-1]

print("l'ordre des taches sur la deuxième machine: ")
for i in range(len(tri)):
    machine2.append(t)
    if(machine1[i]+P1[tri[i]-1]>t):
        t=machine1[i]+P1[tri[i]-1]
        tf=t+P2[tri[i]-1]
    else:
        tf=t+P2[tri[i]-1]
    print(f"t{tri[i]} :[{t},{tf}]")
    t=tf
print(f"Cmax={t}")

### First attempt----------------------------------------------------------------------------------
import numpy as np

print("first attempt to solve our real problem")
n=input("entrez le nombre de produit à fabriquer ")
n=int(n)
m=input("entrez le nombre totale des machines ")
m=int(m)
lin = input("entrez le nombre de lignes de conditionnement")
Nmin= input("Entrez la durée du nettoyage mineur")
Nmaj= input("Entrez la durée du nettoyage majeur")

print("Entrer les temps de traitement de chaque produit sur les machine ")
P=np.zeros((n,m))
stock_sec=[]
lot_size=[]
dem=[]
lots=[]
for i in range(n):
    for j in range(m):
        print("Le temps de traitement du produit",i+1,"sur la machine", j+1)
        k=input()
        P[i,j]=k
    print("Le stock de sécurité du produit " ,i+1)
    s=input()
    stock_sec.append(int(s))
    print("La taille de lot du produit", i+1)
    l=input()
    lot_size.append(int(l))
    print("La demande en produit ", i+1)
    d=input()
    dem.append(int(d))
    
    if (int(d)%int(l)==0):
        lots.append(int(d)//int(l))
        print("le nombre de lots du produit", i+1, "a fabriquer est", int(d)//int(l))
    else:
        lots.append(int(d)//int(l) + 1)
        print("le nombre de lots du produit", i+1, "a fabriquer est", int(d)//int(l) + 1)

l=sum(lots)
print("Nous avons donc ", l, "lot à fabriquer")


### Attempt with mip --------------------------------------------------------------------------
from itertools import product
from mip import Model, BINARY 

n=input("Entrer le nombre de produits à fabriquer ")
n=int(n)
m=input("Entrez le nombre de machines ")
m=int(m)
lin=input("Entrez le nombre de ligne de conditionnement")
lin=int(lin)
mfab=m-lin
times = []
stock_sec=[]
stock_init=[]
lot_size=[]
dem=[]
lots=[]
for i in range(n):
    jtimes=[]
    for j in range (m):
        print("Le temps de traitement de l'opération", j+1, "du produit ",i+1)
        t=input()
        jtimes.append(int(t))
    times.append(jtimes)
    print("Le stock initial du produit " ,i+1)
    init=input()
    stock_init.append(int(init))
    print("Le stock de sécurité du produit " ,i+1)
    s=input()
    stock_sec.append(int(s))
    print("La taille de lot du produit", i+1)
    l=input()
    lot_size.append(int(l))
    print("La demande en produit ", i+1)
    d=input()
    dem.append(int(d))
    
    if (int(d)%int(l)==0):
        lots.append(int(d)//int(l) + int(s) - int(init))
    else:
        lots.append(int(d)//int(l) + 1 + int(s) - int(init)) 
    print("le nombre de lots du produit", i+1, "a fabriquer est", lots[i])


print(times)
# Filling the Fab matrix 
Fab=[]
for i in range(n):
    jfab=[]
    for j in range(mfab):
        if times[i][j] != 0:
            jfab.append(1) #if the product i is processed in the machine j
        else:
            jfab.append(0) #if the product i skips the machine j
    Fab.append(jfab)
print(Fab)
# Fillinf the Cond matrix
Cond=[]
for i in range(n):
    jcon=[]
    for j in range(mfab,m):
        if times[i][j] != 0:
            jcon.append(1) #if the product i can be packaged on that line
        else:
            jcon.append(0) #if the product i can't be packaged on that line
    Cond.append(jcon)
print("con = ",Cond)

#Filling the b matrix
b=[]
r=0
for i in range(n):
    lb=[]
    for l in range(sum(lots)):
        if (l>=r) & (l < r+lots[i]):
            lb.append(1) #the batch l is of the product i
        else:
            lb.append(0)
    b.append(lb)
    r=r+lots[i]
print(b)

#Filling the g matrix
g=[]
r=0
for i in range(n): 
    for l in range(r,r+lots[i]):
        g.append(b[i])
    r= r+lots[i]
print(g)




'''        
machines=[]
for i in range(n):
    jmachines=[]
    for j in range(m):
        print("L'opération", j+1, "du produit", i+1, "se fait sur la machine")
        s=input()
        jmachines.append(int(s)-1)
    machines.append(jmachines)
print(machines)



model = Model('JSSP')

c = model.add_var(name="C")
x = [[model.add_var(name='x({},{})'.format(j+1, i+1)) for i in range(m)] for j in range(n)]
y = [[[model.add_var(name='y({},{},{})'.format(j+1, i+1, k+1))for i in range(m)] 
    for k in range(n)] for j in range(n)]

model.objective = c

for (j, i) in product(range(n), range(1, m)):
    model += x[j][machines[j][i]] - x[j][machines[j][i-1]] >= \
        times[j][machines[j][i-1]]

'''
    ## Fonction de contraintes (don't think it's necessary)
    def allocation(self):
        alloc=[]
        for l in range(sum(self.inst.lots)):
            if (sum(self.X[l])==1):
                alloc.append(True)
            else: return False
        return all(alloc)
    
    def seqfab1(self):
        seq=[]
        for l in range(sum(self.inst.lots)):
            lseq=[]
            for k in range(sum(self.inst.lots)):
                kseq=[]
                if k !=l:
                    for j in range(self.inst.mfab):
                        jseq=[]
                        somme= self.FT[l][j]
                        for i in range(self.prod):
                            somme = somme + self.inst.b[i][l]*self.inst.fab[i][j]*(self.inst.times[i][j]+self.inst.Nmin*self.inst.g[l][k]+self.inst.Nmaj*(1-self.inst.g[l][k]))
                        if somme <= self.FT[k][j]+1000000*(1-self.Y[l][k][j]):
                            jseq.append(True)
                        else: return False
                        kseq.append(jseq)
                    lseq.append(kseq)
            seq.append(lseq)
        return all(seq)

    def seqfab2(self):
        seq=[]
        for l in range(sum(self.inst.lots)):
            lseq=[]
            for k in range(sum(self.inst.lots)):
                kseq=[]
                if k !=l:
                    for j in range(self.inst.mfab):
                        jseq=[]
                        somme= self.FT[k][j]
                        for i in range(self.prod):
                            somme = somme + self.inst.b[i][k]*self.inst.fab[i][j]*(self.inst.times[i][j]+self.inst.Nmin*self.inst.g[l][k]+self.inst.Nmaj*(1-self.inst.g[l][k]))
                        if somme <= self.FT[l][j]+1000000*self.Y[l][k][j]:
                            jseq.append(True)
                        else: return False
                        kseq.append(jseq)
                    lseq.append(kseq)
            seq.append(lseq)
        return all(seq)
    
    def seqcon3(self):
        seq=[]
        for l in range(sum(self.inst.lots)):
            lseq=[]
            for k in range(sum(self.inst.lots)):
                kseq=[]
                if k!=l:
                    for a in range(self.inst.lin):
                        jseq=[]
                        somme= self.CT[l]
                        for i in range(self.prod):
                            somme = somme + self.inst.b[i][l]*(self.inst.pc[i]+self.inst.Nmin*self.inst.g[l][k]+self.inst.Nmaj*(1-self.inst.g[l][k]))
                        if somme <= self.CT[k]+100000000*(1-self.U[l][k][a])+10000000*(2-self.X[l][a]-self.X[k][a]):
                            jseq.append(True)
                        else: return False
                        kseq.append(jseq)
                    lseq.append(kseq)
            seq.append(lseq)
        return all(seq)

    def seqcon2(self):
        seq=[]
        for l in range(sum(self.inst.lots)):
            lseq=[]
            for k in range(sum(self.inst.lots)):
                kseq=[]
                if k !=l:
                    for a in range(self.inst.lin):
                        jseq=[]
                        somme= self.CT[k]
                        for i in range(self.prod):
                            somme = somme + self.inst.b[i][k]*(self.inst.pc[i]+self.inst.Nmin*self.inst.g[l][k]+self.inst.Nmaj*(1-self.inst.g[l][k]))
                        if somme <= self.CT[l]+100000000*self.U[l][k][a]+10000000*(2-self.X[l][a]-self.X[k][a]):
                            jseq.append(True)
                        else: return False
                        kseq.append(jseq)
                    lseq.append(kseq)
            seq.append(lseq)
        return all(seq)


## early exemple

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

