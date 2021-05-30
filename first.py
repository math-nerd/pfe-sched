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