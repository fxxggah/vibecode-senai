# Solicita os dados do aluno
nota = float(input("Digite a nota do aluno: "))
frequencia = float(input("Digite a frequência do aluno: "))

# Estrutura de decisão para classificação do aluno
if (nota >= 50 ) and (frequencia >= 75):
    print("Aluno aprovado!")
    
elif (nota >= 25) or (frequencia >= 60):
    print("Aluno em recuperação!")

else:
    print("Aluno reprovado por nota e frequência!")