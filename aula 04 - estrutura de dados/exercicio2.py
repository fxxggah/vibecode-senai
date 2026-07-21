temperaturas = []

while True:
    temperaturas.append(float(input("Digite a temperatura do ar: ")))

    resposta = input("Deseja continuar? (s/n): ")
    if resposta.lower() == "n" or resposta.lower() == "N":
        break

quantidadeDados = len(temperaturas)
valorMaximo = max(temperaturas)
valorMinimo = min(temperaturas)
valorMedio = sum(temperaturas) / quantidadeDados

print(f"Quantidade de dados: {quantidadeDados}")
print(f"Valor máximo: {valorMaximo:.2f}")   
print(f"Valor mínimo: {valorMinimo:.2f}")
print(f"Valor médio: {valorMedio:.2f}")

if valorMedio < 17:
    print("O clima está frio.")
elif valorMedio >= 17 and valorMedio < 26:
    print("O clima está confortável.")  
else:
    print("O clima está quente.")