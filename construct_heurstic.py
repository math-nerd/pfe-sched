from product import product
from jssp_instance import instance

def colonne(liste, j):
        return[item[j] for item in liste]

class construct_sol:
    def __init__(self, inst): # une objet de la classe instance est donnée comme entrée
        self.inst=inst
        self.Y = [[[0]*inst.L for _ in range(inst.L)] for _ in range(inst.mfab)]
        self.U = [[[0]*inst.L for _ in range(inst.L)] for _ in range(inst.lin)]
        self.X = [[0]*inst.lin for _ in range(inst.L)]

    def goulot(self):
        somme=[sum(colonne(self.inst.times, j)) for j in range(self.inst.m)]
        if somme.index(max(somme)) < self.inst.mfab:
            return 0
        else:
            return 1

    def mach_goulot(self):
        somme=[sum(colonne(self.inst.times, j)) for j in range(self.inst.mfab)]
        return somme.index(max(somme))

    def fill_Y(self, j):
        machg= j
        jtimes=colonne(self.inst.times, machg)
        deja_vu=[]
        for i in range(self.inst.n):
            prod_max=jtimes.index(max(jtimes))
            k=sum(self.inst.lots[0:prod_max]) # nbr de lots avant prod max
            for lot in range(k, k+self.inst.lots[prod_max]):
                deja_vu.append(lot)
                for l in range(self.inst.L) :
                    if not l in deja_vu:
                        self.Y[machg][lot][l]=1
                jtimes[prod_max]=-1
        for j in range(self.inst.mfab):
            self.Y[j] = list(self.Y[machg])

        
    def fill_X(self):
        somme_Y=[sum(self.Y[0][l]) for l in range(self.inst.L)]
        T=[0]*self.inst.lin
        for l in range(self.inst.L):
            ind = somme_Y.index(max(somme_Y))
            list_T=list(T)
            for a in range(self.inst.lin):
                a_i=list_T.index(min(list_T))
                if (sum(self.inst.con[i][a_i]*self.inst.b[i][ind] for i in range(self.inst.n)) == 1):
                    self.X[ind][a_i]=1
                    T[a_i] += sum([self.inst.pc[k] * self.inst.b[k][ind] for k in range(self.inst.n)])
                    break
                else:
                    list_T[a_i] = 100000000
            somme_Y[ind]=-1

    def fill_XU(self):
        T=[0]*self.inst.lin
        somme_con= [sum(self.inst.con[i]) for i in range(self.inst.n)] #connaitre le nombre de ligne disponible pour chaque produit
        deja_vu=[] #les lots déjà ordonancé
        for i in range(self.inst.n):
            lin_min = somme_con.index(min(somme_con)) 
            k= sum(self.inst.lots[0:lin_min]) # nbr de lots avant lin_min
            list_T=list(T)
            for l in range(k, k+self.inst.lots[lin_min]):
                deja_vu.append(l)
                for a in range(self.inst.lin):
                    a_i=list_T.index(min(list_T))
                    for lot in range(self.inst.L):
                        for p in range(self.inst.lin):
                            if lot not in deja_vu:
                                self.U[p][l][lot]=1  
                    if (self.inst.con[lin_min][a_i] == 1):
                        self.X[l][a_i] = 1
                        T[a_i] += sum([self.inst.pc[k] * self.inst.b[k][l] for k in range(self.inst.n)])
                        break
                    else:
                        list_T[a_i]=100000000000
            somme_con[lin_min]=100000
        
    def greedy(self):
        # je veux appliquer la méthode process_input avant de commencer la construction de la solution
        #self.inst.process_input()
        if self.goulot() == 0: ##si l'étape goulot est la fabrication
            machg= self.mach_goulot()
            self.fill_Y(machg)
            for a in range(self.inst.lin):
                self.U[a]= list(self.Y[0])
            self.fill_X()
        else:## Le goulot au niveau du conditionnement 
            self.fill_XU()
            for j in range(self.inst.mfab):
                self.Y[j]= list(self.U[0])

                    

        











mfab=3
lin=2
netmin = 4
netmaj = 18
prod1 = product('produit1', [3, 5, 3, 16, 0], 16, 170, 0, 0,1)
prod2 = product('produit2', [3, 5, 3, 21, 0], 21, 15, 0, 0, 1)
prod3 = product('produit3', [3, 5, 3, 22, 22], 22, 78, 0, 0, 4)
prod4 = product('produit4', [3, 5, 3, 0, 15], 15, 230, 0, 0, 1)
prod5 = product('produit5', [3, 5, 3, 0, 24], 24, 23, 0, 0, 1)
prod6 = product('produit1', [3, 5, 3, 16, 0], 16, 46, 0, 0, 1)

prod=[prod1, prod2, prod3, prod4, prod5, prod6]


jssp = instance(mfab, lin , netmin, netmaj, prod)
jssp.process_input()
sol_init=construct_sol(jssp)
sol_init.greedy()
print("Y = ", sol_init.Y)
print("U = ", sol_init.U)
print("X = ", sol_init.X)
