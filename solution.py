def colonne(liste, j):
    return[item[j] for item in liste]

class solution:
    def __init__(self, inst, X, Y, U):
        self.inst = inst
        self.FT = [[0]*inst.mfab]*sum(inst.lots)
        self.CT = []
        self.Cmax = 0
        self.X = X
        self.Y = Y
        self.U = U
    
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
    
    ## Les autres contraintes semblent être implicite lors de la construction
    ##Think later if you should or not add them


    def get_FT(self): 
        time=[0]*len(self.Y[1]) # La date de fin de l'opération précédente des lots
        for j in range(self.inst.mfab): # On parcourt les machines de fabrication
            somme=[] # pour la matrice Y de la machine j on somme les ligne
            # la ligne avec la plus grande somme correspond au lot qui passe en premier sur cette machine
            for i in range(len(self.Y[j])):
                k=sum(self.Y[j][i])
                somme.append(k)
            indpre = somme.index(max(somme)) #l'indice du lot qui commence en premier 
            ###############THINK 
            r=0 # variable pour ne pas considérer un temps de nettoyage avant le trt le premier lot
            for i in range(len(somme)): # on parcourt tous les lots 
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
        



