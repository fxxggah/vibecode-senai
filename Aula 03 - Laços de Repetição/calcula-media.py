media= 0

for i in range(12):
    valor = float(input(f"Quantas televisoes que vendeu no mês {i + 1}: "))
    media = media + valor

print(f"A média de televisões vendidas no ano foi: {media / 12:.2f}")