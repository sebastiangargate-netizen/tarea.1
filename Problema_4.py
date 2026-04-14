def calcular_imc(peso, altura):
    """
    Calcula el Índice de Masa Corporal (IMC) y lo clasifica según la OMS.
    
    Parámetros:
    peso (float): Peso en kilogramos.
    altura (float): Altura en metros.
    
    Retorna:
    str: La categoría del IMC.
    """
    imc = peso / (altura ** 2)
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"

if __name__ == "__main__":
    peso = float(input("Introduce el peso en kg: "))
    altura = float(input("Introduce la altura en metros: "))
    categoria = calcular_imc(peso, altura)
    print(f"La categoría del IMC es: {categoria}")