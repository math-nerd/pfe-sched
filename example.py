from product import product

def two_var():
  A = product('produit1', [2, 3, 2, 18, 0], 18, 1, 0, 0,1)
  B = "sup"
  return A,B

C=two_var()
print(C)
print(C[0].name)
print(C[1])

F= [2, 3, 2, 18, 0]
F.pop()
print(F)
print(5 not in F)