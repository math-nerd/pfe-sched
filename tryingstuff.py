import math
#print(int(math.ceil(4.1)))
def colonne(liste, j):
    return[item[j] for item in liste]

F= [[1, 4,7], 
    [3,5,6], [3,1,18]]
b=[1,5]
print(colonne(F, 1))
