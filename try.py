from itertools import product
from mip import Model, BINARY 

n=input("Entrer le nombre de produits à fabriquer ")
n=int(n)
m=input("Entrez le nombre de machine ")
m=int(m)
times = []

for i in range(n):
    jtimes=[]
    for j in range (m):
        print("Le temps de traitement de l'opération", j+1, "du produit ",i+1)
        t=input()
        jtimes.append(int(t))
    times.append(jtimes)

print(times)
        
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

