# Criação da matriz 3x4 com entrada do usuário

matriz = []
linhas = 3
colunas = 4

print("Digite os valores para uma matriz 3x4:")

for i in range(linhas):
    linha = []
    for j in range(colunas):
        valor = int(input(f"Digite o valor para posição [{i}][{j}]: "))
        linha.append(valor)
    matriz.append(linha)

# Inicialização dos valores de maior e menor

maior = matriz[0][0]
menor = matriz[0][0]
pos_maior = (0, 0)
pos_menor = (0, 0)

# Busca pelos valores

for i in range(linhas):
    for j in range(colunas):
        if matriz[i][j] > maior:
            maior = matriz[i][j]
            pos_maior = (i, j)
        if matriz[i][j] < menor:
            menor = matriz[i][j]
            pos_menor = (i, j)

# Exibição dos resultados

print("\nMatriz inserida:")
for linha in matriz:
    print(linha)

print(f"\nMaior valor: {maior} na posição (linha {pos_maior[0]}, coluna {pos_maior[1]})")
print(f"Menor valor: {menor} na posição (linha {pos_menor[0]}, coluna {pos_menor[1]})")
