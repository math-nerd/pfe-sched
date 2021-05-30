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








