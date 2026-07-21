# Criação dos dicionários com os dados de cada pessoa

pessoa1 = {
    "nome": "João",
    "sobrenome": "Silva",
    "cpf": "123.456.789-00",
    "rg": "12.345.678-9",
    "data_nascimento": "10/05/2000",
    "telefone": "(11) 99999-1111",
    "endereco": "Rua das Flores, 100"
}

pessoa2 = {
    "nome": "Maria",
    "sobrenome": "Oliveira",
    "cpf": "987.654.321-00",
    "rg": "98.765.432-1",
    "data_nascimento": "22/08/1998",
    "telefone": "(11) 98888-2222",
    "endereco": "Av. Central, 250"
}

pessoa3 = {
    "nome": "Carlos",
    "sobrenome": "Souza",
    "cpf": "111.222.333-44",
    "rg": "55.666.777-8",
    "data_nascimento": "15/12/1995",
    "telefone": "(11) 97777-3333",
    "endereco": "Rua do Sol, 50"
}

# Lista que armazena os três dicionários
cadastroPessoas = [pessoa1, pessoa2, pessoa3]

# Exibe todas as pessoas cadastradas
for pessoa in cadastroPessoas:
    print("Nome:", pessoa["nome"], pessoa["sobrenome"])
    print("CPF:", pessoa["cpf"])
    print("RG:", pessoa["rg"])
    print("Data de Nascimento:", pessoa["data_nascimento"])
    print("Telefone:", pessoa["telefone"])
    print("Endereço:", pessoa["endereco"])
    print("-" * 30)