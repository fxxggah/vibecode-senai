import statistics

temperaturas = []

for i in range(10):
    temperatura = float(input(f"Digite a {i + 1}ª temperatura: "))
    temperaturas.append(temperatura)

maior = max(temperaturas)
menor = min(temperaturas)
media = statistics.mean(temperaturas)

print("\nResultados:")
print(f"Maior temperatura: {maior:.2f}°C")
print(f"Menor temperatura: {menor:.2f}°C")
print(f"Temperatura média: {media:.2f}°C")