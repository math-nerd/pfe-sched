import math
#print(int(math.ceil(4.1)))

F= [[1, 4,7], [3,5,6], [3,1,18]]
b=[1,5]
"""
#print(F.extend(b))
mini=[]
indice=[]
for j in range(3):
    jmini=[]
    for i in range(3):
        jmini.append(F[i][j])
    indice.append(jmini.index(min(jmini)))
    mini.append(min(jmini))
print(mini)
print(indice)
"""
T=[[1,2,4], [1,6,7], [6,7,8]]
C= T.pop(1)
print(T)
print(C)
