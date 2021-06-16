import math 
class product:
 
    def __init__(self, name, pt, pc, dem, sinit, ssec, lsize):
        self.name = name
        self.pt = pt
        self.pc = pc
        self.dem = dem
        self.sinit= sinit
        self.ssec =  ssec
        self.lsize = lsize
        self.lots = int(math.ceil(self.dem/self.lsize)) + self.ssec - self.sinit


prod1 = product("semcta", [1, 2, 4], [12, 12], 60, 4, 2,4)
print(prod1.lots)
