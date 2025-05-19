pessoa = {
  "nome": "Teste",
   "peso": 0.0,
   "idade": 0
}

print("Dados da pessoa:")
print("Nome:", pessoa["nome"])
print("Peso:", pessoa["peso"])
print("Idade:", pessoa["idade"])

pessoa["nome"] = "Texto"
pessoa["peso"] = 99.99
pessoa["idade"] = 10

print("Nome:", pessoa["nome"])
print("Peso:", pessoa["peso"])
print("Idade:", pessoa["idade"])

pessoa["nome"] = input("Digite seu nome:")
pessoa["peso"] = float(input("Digite seu peso:"))
pessoa["idade"] = int(input("Digite sua idade:"))

print("Dados da pessoa:")
print("Nome:", pessoa["nome"])
print("Peso:", pessoa["peso"])
print("Idade:", pessoa["idade"])
