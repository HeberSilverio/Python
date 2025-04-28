# Outro jeito de fazer o contador

contador = 0

while True:
    print("Contador atual:", contador)
    print("Escolha uma opção:")
    print("[1] Incrementar contador")
    print("[2] Encerrar programa")

    escolha = input("Digite sua escolha: ")

    if escolha == '1':
        contador += 1
        continue  # Volta para o início do loop
    if escolha == '2':
        print("Encerrando o programa...")
        break  # Sai do loop
    print("Opção inválida! Tente novamente.")
    continue  # Volta para o início se digitou errado
