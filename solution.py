class solution:
    def __init__(self, inst, FT, CT, Cmax, X, Y, U):
        self.inst = inst
        self.FT = FT
        self.CT = CT
        self.Cmax = Cmax
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
                if k !=l:
                    for a in range(self.inst.lin):
                        jseq=[]
                        somme= self.CT[l]
                        for i in range(self.prod):
                            somme = somme + self.inst.b[i][l]*(self.inst.pc[i]+self.inst.Nmin*self.inst.g[l][k]+self.inst.Nmaj*(1-self.inst.g[l][k]))
                        if somme <= self.CT[k]+100000000*(1-self.U[l][k][j])+10000000*(2-self.X[l][a]-self.X[k][a]):
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
                        if somme <= self.CT[l]+100000000*self.U[l][k][j]+10000000*(2-self.X[l][a]-self.X[k][a]):
                            jseq.append(True)
                        else: return False
                        kseq.append(jseq)
                    lseq.append(kseq)
            seq.append(lseq)
        return all(seq)
    
    #def seqord(self):
