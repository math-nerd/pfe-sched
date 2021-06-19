from product import product
from jssp_instance import instance
def colonne(liste, j):
    return[item[j] for item in liste]

class solution: 
    def __init__(self, inst, X, Y, U):
        self.inst = inst
        self.FT = [[0]*inst.mfab]*sum(inst.lots)
        self.CT = [0]*sum(inst.lots)
        self.Cmax = 0
        self.X = X # matrice lot*lines de conditionnement =1 si le lot i est conditionné sur la ligne a
        self.Y = Y # liste de liste de listes =1 si le lot l est traité avant le lot l' sur la machine j
        self.U = U # liste de liste de listes =1 si le lot l est conditionné avant le lot l' sur la ligne a
    
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
        """
    
    ## Les autres contraintes semblent être implicite lors de la construction
    ##Think later if you should or not add them


    def get_FT(self): 
        time=[0]*len(self.Y[0]) # La date de fin de l'opération précédente des lots
        for j in range(self.inst.mfab): # On parcourt les machines de fabrication
            somme=[] # la ligne avec la plus grande somme correspond au lot qui passe en premier sur cette machine
            for i in range(len(self.Y[j])):
                k=sum(self.Y[j][i])
                somme.append(k)
            indpre = somme.index(max(somme)) #l'indice du lot qui commence en premier 
            ###############THINK  
            r=0 # variable pour ne pas considérer un temps de nettoyage avant le trt le premier lot
            for i in range(len(somme)): # on parcourt tous les lots 
                FT1 = self.FT[indpre][j] + 
                FT2 = 

                ind=somme.index(max(somme)) # indice du lot qu'on va ordonnancer 
                g = self.inst.g[ind][indpre] # vérifier si le lot actuel est du même produit que le lot précédent

                #le temps de début du trt du lot ind est le temps de la fin du trt du lot précendent plus le temps de nettoyage
                #on multiplie par fab pour être sur que le lot passe par la machine j et donc un nettoyage est nécessaire

                time = time + (g*self.inst.netmin + (1-g)*self.inst.netmaj)*r* sum([self.inst.b[k][ind] * self.inst.fab[k][j] for k in range(self.inst.n)])
                self.FT[ind][j]= time
                #On rajoute le temps de traitement du lot ind sur la machine j pour avoir le temps de fin de traitement 
                time = time + sum([self.inst.times[k][j] * self.inst.b[k][ind] for k in range(self.inst.n)])
                indpre = ind # on affect l'indice du lot actuel à la variable de l'indice précédent
                somme[ind] = -1 # écrasez la valeur maximal pour trouver l'autre valeur à la prochaine itération
                r=1 
            time = colonne(self.FT, j)
            """

    def fillFT(self):
        last_time = [0]*len(self.Y[0])
        c=0
        for j in range(self.inst.mfab):
            somme=[]
            for i in range(len(self.Y[j])):
                k=sum(self.Y[j][i])
                somme.append(k)
            indpre = somme.index(max(somme))
            r=0
            for i in range(sum(self.inst.lots)):
                ind=somme.index(max(somme)) 
                g = self.inst.g[ind][indpre]
                FT1=last_time[ind] 
                FT2= self.FT[indpre][j] + sum([self.inst.times[k][j] * self.inst.b[k][indpre] for k in range(self.inst.n)])*c + (g*self.inst.netmin + (1-g)*self.inst.netmaj)*r
                self.FT[ind][j]= max([FT1, FT2])
                indpre=ind
                somme[indpre]=-1
                r=1
                
            last_time = colonne(self.FT, j)
            for l in range(len(last_time)):
                last_time[l] += sum([self.inst.times[k][j] * self.inst.b[k][l] for k in range(self.inst.n)])
            c=1

        
## Exemple
mfab=3
lin=2
netmin = 12
netmaj = 24
prod1 = product('produit1', [2, 3, 4, 12, 0], 12, 100, 0, 0, 100)
prod2 = product('produit2', [2, 1, 5, 0, 10], 10, 2000, 0, 0, 2000)
prod3 = product('produit3', [1, 2, 0, 6, 0], 6, 1500, 0, 0, 1500)
prod4 = product('produit4', [2, 3, 0, 0, 7], 7, 1000, 0, 0, 1000)
prod5 = product('produit5', [1, 3, 4, 14, 14], 14, 250, 0, 0, 250)
prod6 = product('produit1', [2, 1, 0, 10, 10], 10, 200, 0, 0, 200) 
prod=[prod1, prod2, prod3, prod4, prod5, prod6]
jssp = instance(mfab, lin , netmin, netmaj, prod)
jssp.process_input()
X=[[1, 0],[0, 1],[1, 0],[0, 1],[0, 1],[0, 1]]
Y= [[[0, 0, 1, 1, 0, 1,],[1, 0, 1, 1, 0, 1],[0, 0, 0, 0, 0, 0],[0, 0, 1, 0, 0, 0],[1, 1, 1, 1, 0, 1],[0, 0, 1, 1, 0, 0]],
    [[0, 0, 1, 1, 0, 1],[1, 0, 1, 1, 0, 1],[0, 0, 0, 0, 0, 0],[0, 0, 1, 0, 0, 0],[1, 1, 1, 1, 0, 1],[0, 0, 1, 1, 0, 0]],
    [[0, 0, 1, 1, 0, 0],[1, 0, 1, 1, 0, 1],[0, 0, 0, 0, 0, 0],[0, 0, 1, 0, 0, 0],[1, 1, 1, 1, 0, 1],[1, 0, 1, 1, 0, 0]]]

U=[[[0, 0, 1, 0, 1, 1],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 1, 0],[0, 0, 0, 0, 0, 0],[0, 0, 1, 0, 0, 1],[0, 0, 1, 0, 0, 0]],
    [[0, 0, 0, 0, 0, 0],[0, 0, 0, 1, 0, 1],[0, 0, 0, 0, 0, 0],[0, 0, 0, 0, 0, 0],[0, 1, 0, 1, 0, 1],[0, 0, 0, 1, 0, 0]]]
sol1=solution(jssp,X, Y, U )

#print(sol1.inst.b)
#sol1.fillFT()
print(sol1.FT)

last_time = [0]*len(sol1.Y[0])
print('last time début =', last_time)

for j in range(sol1.inst.mfab):
    somme=[]
    for i in range(len(sol1.Y[j])):
        k=sum(sol1.Y[j][i])
        somme.append(k)
    print("somme de ", j, "égal à", somme)
    indpre = somme.index(max(somme))
    print("le lot qui commence à la machine", j,"est ", indpre)
    r=0
    c=0
    for i in range(sum(sol1.inst.lots)):
        ind=somme.index(max(somme))
        print("indice considéré à cette étape est", ind) 
        g = sol1.inst.g[ind][indpre]
        FT1=last_time[ind] 
        FT2= sol1.FT[indpre][j] + sum([sol1.inst.times[k][j] * sol1.inst.b[k][indpre] for k in range(sol1.inst.n)])*c + (g*sol1.inst.netmin + (1-g)*sol1.inst.netmaj)*r
        sol1.FT[ind][j]= max([FT1, FT2])
        print("La matrice FT ressemble à )",sol1.FT)
        print("le temps de début du traitement du lot", ind, "sur la machine", j, "est", max([FT1,FT2]))
        indpre=ind
        somme[indpre]=-1
        print(somme)
        r=1
        c=1
                
    last_time = colonne(sol1.FT, j)
    print(last_time)
    for l in range(len(last_time)):
        last_time[l] += sum([sol1.inst.times[k][j] * sol1.inst.b[k][l] for k in range(sol1.inst.n)])
    print("les temps de fin de trt sur la machine", j, last_time)
    


