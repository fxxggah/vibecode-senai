#Lista vazia.
convidados = []

#Adicionando 5 convidados na lista.
convidados.append("Lucas")
convidados.append("Roberto")
convidados.extend(["Maria", "Joaquina", "Cacilda"])

#Edita um convidado da lista
convidados[0] = "Lukas"
convidados[-1] = "Gertrudes"

#Remove um convidado da lista
convidados.remove("Maria")
convidados.pop(2)

# Exibe todos os convidados
for pessoa in convidados:
    print(pessoa)