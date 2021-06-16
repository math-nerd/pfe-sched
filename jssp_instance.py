from product import product
class instance :

    def __init__ (self, mfab, n, lin , prod):
        self.n = n
        self.prod = prod
        self.lin = lin
        self.mfab= mfab
        self.times =[]
        self.b=[]
        self.g = []
        self.fab=[]
        self.con=[]
        self.lots=[]
        self.pc=[]

    def filltimes(self):
        for i in range(self.n):
            self.times.append(self.prod.times)
            """
            jtimes=[]
            for j in range (self.mach):
                print("Le temps de traitement de l'opération", j+1, "du produit ",i+1)
                t=input()
                jtimes.append(int(t))
            self.times.append(jtimes)
            self.lots.append(self.dem + int(self.sec) - int(self.sinit))
    """
    def fillfab(self):
        for i in range(self.prod):
            jfab=[]
            for j in range(self.mfab):
                if self.times[i][j] != 0:
                    jfab.append(1) #if the product i is processed in the machine j
                else:
                    jfab.append(0) #if the product i skips the machine j
            self.fab.append(jfab)
        return self.fab 
    
    def fillcon(self):
        for i in range(self.prod):
            jcon=[]
            for j in range(self.mfab,self.mach):
                if self.times[i][j] != 0:
                    jcon.append(1) #if the product i can be packaged on that line
                else:
                    jcon.append(0) #if the product i can't be packaged on that line
            self.cond.append(jcon)
        return self.cond 
    
    def fillb(self):
        r=0
        for i in range(self.prod):
            lb=[]
            for l in range(sum(self.lots)):
                if (l>=r) & (l < r+self.lots[i]):
                    lb.append(1) #the batch l is of the product i
                else:
                    lb.append(0)
            self.b.append(lb)
            r=r+self.lots[i]
        return self.b  

    def fillg(self):
        r=0
        for i in range(self.prod): 
            for l in range(r,r+self.lots[i]):
                self.g.append(self.b[i])
            r= r+self.lots[i]
        return self.g
