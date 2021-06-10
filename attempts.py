# Filling the Fab matrix 
n=3
m=5
mfab=3
times=[[13, 14, 15, 12, 34], [11, 12,0,12,0], [11,0,10,0,19]]
lots=[2, 3, 1]
b=[[1, 1, 0, 0, 0, 0], [0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1]]
g=[]
r=0
# Fillinf the Cond matrix
Cond=[]
for i in range(n):
    jcon=[]
    for j in range(mfab,m):
        if times[i][j] != 0:
            jcon.append(1) #if the product i can be packaged on that line
        else:
            jcon.append(0) #if the product i can't be packaged on that line
    Cond.append(jcon)
print(Cond)
print(list(range(mfab,m)))

