# Programa que pede números até o usuário digitar 0

while True:
    numero = int(input("Digite um número (0 para sair): "))
    if numero == 0:
        print("Programa encerrado.")
        break
