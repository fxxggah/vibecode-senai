def opcoes():
    print("Selecione uma opção")
    print("1 - Calcular área do triangulo")
    print("2 - Calcular área do cículo")

    resposta = int(input("Opção selecionada: "))
    return resposta

def  calcular_area_retangulo (base, altura):
    area = base * altura
    return area

def calcular_area_circulo (raio):
    area = 3.1416 * (raio ** 2)
    return area

def calcular_area_triangulo_equilatero (base, altura):
    area = (base * altura) / 2
    return area