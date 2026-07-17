import utils

utils.exibir_menu()

opcao = input("Escolha uma opção (1-5): ").strip()

if opcao == '5':
    print("Saindo do programa de Matemática Básica. Até logo!")
    
if opcao in ['1', '2', '3', '4']:
    num1 = int(input("Digite o primeiro número inteiro: "))
    num2 = int(input("Digite o segundo número inteiro: "))
    
    if opcao == '1':
        resultado = utils.somar(num1, num2)
        operacao = "+"
    elif opcao == '2':
        resultado = utils.subtrair(num1, num2)
        operacao = "-"
    elif opcao == '3':
        resultado = utils.multiplicar(num1, num2)
        operacao = "*"
    elif opcao == '4':
        resultado = utils.dividir(num1, num2)
        operacao = "/"
        
    if resultado is None and operacao == "/":
        print("\nErro: Divisão por zero não é permitida!")
    else:
        print(f"\nResultado: {num1} {operacao} {num2} = {resultado}")
else:
    print("\nOpção inválida! Por favor, escolha uma opção entre 1 e 5.")
