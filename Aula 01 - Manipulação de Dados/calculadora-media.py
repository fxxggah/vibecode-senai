nome = input("Digite o nome do aluno: ")

nota1 = float(input("Digite a 1ª nota: "))
nota2 = float(input("Digite a 2ª nota: "))
nota3 = float(input("Digite a 3ª nota: "))
nota4 = float(input("Digite a 4ª nota: "))

media = (nota1 + nota2 + nota3 + nota4) / 4

print(f"\nAluno: {nome}")
print(f"Média final: {media:.2f}")