def exibir_menu():
    print("\n--- Conversor de Temperatura ---")
    print("1. Celsius para Fahrenheit")
    print("2. Celsius para Kelvin")
    print("3. Sair")

def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

def celsius_para_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin