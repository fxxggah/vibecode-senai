for i in range(6):

    print("-----")

    nome = input("Digite o nome do aluno: ")
    nota = float(input(f"Digite a nota do(a) {nome}: "))

    if nota >= 7:
        print(f"{nome} foi aprovado(a)")
    else:
        print(f"{nome} foi reprovado(a)")

    resposta = input("Deseja continuar? (S/N): ")

    if resposta.upper() == "N":
        break