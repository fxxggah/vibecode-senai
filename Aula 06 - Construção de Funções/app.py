import utils

while True:

    resposta = utils.opcoes()


    if resposta == 1:

        base = float(input("Digite a base de um retangulo em cm: "))
        altura = float(input("Digite a altura do retangulo em cm: "))

        area = utils.calcular_area_retangulo(base, altura)

        print(f"A área do retangulo é: {area}cm²")

    elif resposta == 2:

        raio = float(input("Digite o raio de um retangulo em cm: "))

        area = utils.calcular_area_circulo(raio)

        print(f"A área do círculo é: {area}cm²")

    elif resposta == 3:

        base = float(input("Digite a base de um retangulo em cm: "))
        altura = float(input("Digite a altura do retangulo em cm: "))

        area = utils.calcular_area_triangulo_equilatero(base, altura)

        print(f"A área do retangulo equilatero é: {area}cm²")

    else:
        print("Resposta inválida")

    continuar = input("Deseja continuar? (S/N): ")

    if ((continuar.upper)) == "N": break