import copy
def colonne(liste, j):
    return[item[j] for item in liste]

class solution: 
    def __init__(self, inst, X, Y, U):
        self.inst = inst
        self.FT = []
        self.CT = [0]*sum(inst.lots)
        self.Cmax = 0
        self.finfab=[]
        self.fincon=[] 
        self.X = X # matrice lot*lines de conditionnement =1 si le lot i est conditionné sur la ligne a
        self.Y = Y # liste de liste de listes =1 si le lot l est traité avant le lot l' sur la machine j
        self.U = U # liste de liste de listes =1 si le lot l est conditionné avant le lot l' sur la ligne a
    
            
    def fill_FT(self):
        last_time = [0]*len(self.Y[0])
        FT=[]
        k=0
        for j in range(self.inst.mfab):
            somme=[]
            for i in range(len(self.Y[j])):
                k=sum(self.Y[j][i])
                somme.append(k)
            indpre = somme.index(max(somme))
            c=0
            liste = [0]*len(somme)
            for i in range(sum(self.inst.lots)):
                ind=somme.index(max(somme)) 
                g = self.inst.g[ind][indpre]
                FT1=last_time[ind] 
                k = sum([self.inst.fab[k][j] * self.inst.b[k][indpre] * (self.inst.times[k][j] + g*self.inst.netmin[0] + (1-g)*self.inst.netmaj[0]) for k in range(self.inst.n)])*c 
                FT2= liste[indpre] + sum([self.inst.fab[k][j] * self.inst.b[k][indpre] * (self.inst.times[k][j] + g*self.inst.netmin[0] + (1-g)*self.inst.netmaj[0]) for k in range(self.inst.n)])*c 
                liste[ind] = max([FT1, FT2])
                indpre=ind
                somme[indpre]=-1
                c=1
            self.FT.append(liste)
            last_time = copy.deepcopy(liste)
            for l in range(len(last_time)):
                pt=sum([self.inst.times[k][j] * self.inst.b[k][l] for k in range(self.inst.n)]) 
                last_time[l] += pt       
        self.FT= list(map(list, zip(*self.FT)))
        self.finfab = copy.deepcopy(last_time)

    def fill_CT(self):
        for a in range(self.inst.lin):
            xcol=colonne(self.X,a)
            pack=[] #vecteur des indices des lots qui vont passer par la ligne a
            for i in range(len(xcol)):
                if xcol[i]==1:
                    pack.append(i)
            somme=[]
            for i in pack:
                somme.append(sum(self.U[a][i]))
            indpre= pack[somme.index(max(somme))]
            c=0
            for l in pack:
                ind = pack[somme.index(max(somme))]
                g = self.inst.g[ind][indpre]
                CT1=self.finfab[ind]
                CT2=self.CT[indpre] + sum([self.inst.con[k][a] * self.inst.b[k][indpre] * (self.inst.pc[k] + g*self.inst.netmin[1] + (1-g)*self.inst.netmaj[1]) for k in range(self.inst.n)])*c
                self.CT[ind] = max([CT1, CT2])
                indpre=ind
                somme[pack.index(ind)]=-1
                c=1

    def get_Cmax(self):
        self.fincon =[]
        for l in range(len(self.CT)):
            k=self.CT[l]+sum([self.inst.pc[k] * self.inst.b[k][l] for k in range(self.inst.n)]) 
            self.fincon.append(k)
        self.Cmax=max(self.fincon)

    def decode(self):
        self.fill_FT()
        self.fill_CT()
        self.get_Cmax()

