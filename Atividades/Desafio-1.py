# Solicita os três números com casas decimais
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

# Calcula a média
media = (num1 + num2 + num3) / 3

# Mostra o resultado formatado com duas casas decimais
print(f"A média dos números é: {media:.2f}")