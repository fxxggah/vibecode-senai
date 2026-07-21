# Dicionário vazio
carros = {}

# Adiciona 3 informações ao dicionário
carros["modelo"] = "Impala"
carros["marca"] = "Chevrolet"
carros["placa"] = "FYI-0234"
carros["preço"] = 50000.00

# Edita o preço de venda do carro
carros.update({"preço": 49000.00})

# Excluir um item do dicionário
carros.pop("placa")

# Exibe todas as informações do dicionário

for chave, valor in carros.items():
    print(f"{chave} = {valor}")