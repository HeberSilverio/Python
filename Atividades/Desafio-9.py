mat = [
   [1, 2, 3, 4],
   [5, 6, 7, 8], 
   [9, 10, 11, 12]
]

maior = mat[0][0]
menor = mat[0][0]
pos_maior = (0, 0)
pos_menor = (0, 0)

print("Os maiores e numeros")
for i in range(len(mat)):
   for j in range(len(mat[i])):
      if mat[i][j] > maior:
         maior = mat[i][j]
         pos_maior = (i, j)
      if mat[i][j] < menor:
         menor = mat[i][j]
         pos_menor = (i, j)