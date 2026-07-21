import utils

utils.exibir_menu()

opcao = input("Escolha uma opção (1-3): ")

if opcao == '3':
    print("Saindo do Conversor de Medidas. Até logo!")
    
if opcao in ['1', '2']:
    celsius = float(input("Digite a temperatura em Celsius (°C) a ser convertida: "))
    
    if opcao == '1':
        resultado = utils.celsius_para_fahrenheit(celsius)
        print(f"\nResultado: {celsius}°C é igual a {resultado:.2f}°F")
    elif opcao == '2':
        resultado = utils.celsius_para_kelvin(celsius)
        print(f"\nResultado: {celsius}°C é igual a {resultado:.2f}K")
else:
    print("\nOpção inválida! Por favor, escolha uma opção entre 1 e 3.")
