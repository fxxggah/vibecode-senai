vendas = [150, 200, 100, 300, 175, 90, 400, 120, 230]

#Valor total de vendas
total_vendas = sum(vendas)

#Valor médio de vendas por dia
media_vendas = total_vendas / len(vendas)

#Maior valor de venda
maior_venda = max(vendas)

#Menor valor de venda
menor_venda = min(vendas)

print(f"O valor total de vendas é: R${total_vendas:.2f}")
print(f"O valor médio de vendas por dia é: R${media_vendas:.2f}")
print(f"A maior venda foi de: R${maior_venda:.2f}")
print(f"A menor venda foi de: R${menor_venda:.2f}")
