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