from product import product 
from jssp_instance import instance
mfab = 3
n = 6
lin = 2
netmin = [0.5, 1]
netmaj = [4, 16]

dem1 = [153900, 153900, 153900, 184680, 184680, 184680, 153900, 153900, 153900, 153900, 153900, 153900]
dem2 = [2217, 22167, 22167, 26600, 26600, 26600, 22167, 22167, 22167, 22167, 22167, 22167]
dem3 = [82903]*12
dem4 = [100146]*12
dem5 = [25000] *12
dem6 = [41667, 41667, 41667, 50000, 50000, 50000, 41667, 41667, 41667, 41667, 41667, 41667]
jssp = []
for i in range(12):
    prod1 = product("Produit1", [3, 5, 3, 32, 0], 32, dem1[i], 14, 14, 12000*0.95)
    prod2 = product("Produit2", [3, 5, 3, 42, 0], 42, dem2[i], 6, 6, 20000*0.95 )
    prod3 = product("Produit3", [3, 5, 3, 44, 44], 44, dem3[i], 0, 0, 13600*0.94)
    prod4 = product("Produit4", [3, 5, 3, 0, 30], 30, dem4[i], 0, 0, 5500*0.95)
    prod5 = product("Produit5", [3, 5, 3, 0, 48], 48, dem5[i], 0, 0, 13750*0.95)
    prod6 = product("Produit6", [3, 5, 3, 32, 0], 32, dem6[i], 0, 0, 12000*0.95)
   

    prod = [prod1, prod2, prod3, prod4,prod5,prod6]
    jssp_i = instance(mfab, lin, netmin, netmaj, prod)
    jssp_i.process_input()
    jssp.append(jssp_i)

