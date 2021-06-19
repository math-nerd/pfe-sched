import math 
m = 5
n = 6

def colonne(liste, j): ## fonction pour avoir la colonne j+1 d'une matrice (liste de listes)
    return[item[j] for item in liste]

class product: # classe des produit
    def __init__(self, name, pt, pc, dem, sinit, ssec, lsize):
        self.name = name
        self.pt = pt
        self.pc = pc
        self.dem = dem
        self.sinit= sinit
        self.ssec =  ssec
        self.lsize = lsize
        self.lots = int(math.ceil(self.dem/self.lsize)) + self.ssec - self.sinit #clacul de nombre de lots à fabriquer


