media = 0
total_produzido = 0
meta = 20000

for i in range(1, 5):
    quantidade = int(input(f"Digite a quantidade de máscaras produzidas na {i}° semana: "))
    total_produzido = total_produzido + quantidade
    media = media + quantidade

if quantidade >= meta:
    print(f"{total_produzido} Máscaras produzidas no mes: META BATIDA!!")
else:
    print(f"{total_produzido} Máscaras produzidas no mes: A META NÃO FOI BATIDA :/")