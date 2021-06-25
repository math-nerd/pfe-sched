import math
#print(int(math.ceil(4.1)))
def colonne(liste, j):
    return[item[j] for item in liste]

def put_colonne(list,i, j, val):
    list[i][j] = val
    return list
F= [[1, 4,7], 
    [3,5,6], [3,1,18]]
b=[1,5]
F[1][1]=16

def colonne(liste, j):
    return[item[j] for item in liste]


X=[[0, 0],[0, 1],[1, 0],[0, 1],[0, 1],[0, 1]]
Y=colonne(X, 0)