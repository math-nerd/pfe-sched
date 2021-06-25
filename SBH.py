def greedy_shift(inst) :
    timean=[]
    for j in range(inst.m): # j machines 
        som=0 
        for i in range(inst.n): # i nbr de produits
            som=som+inst.lots[i] *inst.times(i,j) #lots renvoie nbr de lots du produit i
        
        timean.append(som/sum(inst.lots)) 


    idmax=timean.index(max(timean))

    idprod=inst.times[idmax].index(max(inst.times[idmax])) #indice du produit ayant le plus grand Pi

    Y=[[0]*sum(inst.lots)]*sum(inst.lots) # Y mat de seq du la machine goulot 1

    k=sum(inst.lots[0:idprod]) # nbr de lots avant idprod 

    for i in range(k,k+inst.lots[idprod]) : # parcourir Y sur les indices des lignes du produit de la machine goulot 1

        for l in range(sum(inst.lots)) :
            if (l<k) | (l>i) :
                Y[i][l]=1 


def greedy_shift(inst) :
    timean=[]
    for j in range(inst.m): # j machines 
        som=0 
        for i in range(inst.n): # i nbr de produits
            som=som+inst.lots[i] *inst.times(i,j) #lots renvoie nbr de lots du produit i
        
        timean.append(som/sum(inst.lots)) 


    idmax=timean.index(max(timean))

    idprod=inst.times[idmax].index(max(inst.times[idmax])) #indice du produit ayant le plus grand Pi

    Y=[[0]*sum(inst.lots)]*sum(inst.lots) # Y mat de seq du la machine goulot 1

    k=sum(inst.lots[0:idprod]) # nbr de lots avant idprod 

    for i in range(k,k+inst.lots[idprod]) : # parcourir Y sur les indices des lignes du produit de la machine goulot 1

        for l in range(sum(inst.lots)) :
            if (l<k) | (l>i) :
                Y[i][l]=1 