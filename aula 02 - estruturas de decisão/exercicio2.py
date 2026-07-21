salarioMensal = float(input("Digite o salário mensal: "))

if (salarioMensal < 1400.00):
    print("Situação de risco!")

elif (salarioMensal >= 1400.00 and salarioMensal < 2799.00):
    print("Renda baixa!")

elif (salarioMensal >= 2800.00 and salarioMensal < 6999.00):
    print("Renda média!")
else:
    print("Renda alta!")