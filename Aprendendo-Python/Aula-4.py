idade = 0
altura = 0.0
nome = ""

# Solicita os dados ao usuário
id = int(input("Informe o ID (número inteiro): "))
nome = input("Informe o nome: ")
salario = float(input("Informe o salário (número com ponto para decimais): "))
brasileiro = input("É brasileiro? (s/n): ").strip().lower() == 's'

# Imprime os dados usando f-string
print(f"\nDados informados:\nID: {id}\nNome: {nome}\nSalário: R${salario:.2f}\nBrasileiro: {brasileiro}")
