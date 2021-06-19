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
