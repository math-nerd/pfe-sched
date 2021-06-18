class fonction:

    def fabfill(n,mfab,times):
        Fab=[]
        for i in range(n):
            jfab=[]
            for j in range(mfab):
                if times[i][j] != 0:
                    jfab.append(1) #if the product i is processed in the machine j
                else:
                    jfab.append(0) #if the product i skips the machine j
            Fab.append(jfab)
        return Fab
    

    def confill(n,m,times):
        Cond=[]
        for i in range(n):
            jcon=[]
            for j in range(mfab,m):
                if times[i][j] != 0:
                    jcon.append(1) #if the product i can be packaged on that line
                else:
                    jcon.append(0) #if the product i can't be packaged on that line
            Cond.append(jcon)
        return Cond
    
    def bfill(n,lots):
        b=[]
        r=0
        for i in range(n):
            lb=[]
            for l in range(sum(lots)):
                if (l>=r) & (l < r+lots[i]):
                    lb.append(1) #the batch l is of the product i
                else:
                    lb.append(0)
            b.append(lb)
            r=r+lots[i]
        return b 