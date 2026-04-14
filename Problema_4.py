def pregunta_4(peso: int, altura: float) -> str:
    """
    Parametros:
    peso (float): Peso en kilogramos (kg).
    altura (float): Altura en metros (m).
    Retorna:
    str : La categoria del IMC segun la OMS.
    """
    imc = peso / (altura * altura)

    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"