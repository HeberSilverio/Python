# Criando a lista para armazenar os números
numeros = []

while True:
    # Solicitando um número ao usuário
    num = int(input("Digite um número inteiro (0 para parar): "))
    
    if num == 0:
        break  # Se for 0, interrompe o loop
    
    numeros.append(num)  # Adiciona o número à lista

# Verifica se a lista não está vazia antes de calcular min e max
if numeros:
    print(f"\nQuantidade de números digitados: {len(numeros)}")
    print(f"Maior número digitado: {max(numeros)}")
    print(f"Menor número digitado: {min(numeros)}")
else:
    print("\nNenhum número válido foi digitado.")
