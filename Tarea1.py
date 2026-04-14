from math import pi, sqrt

def pregunta_1(radio: float, angulo: float) -> float:
    return round(radio * angulo * pi / 180, 2)

def pregunta_2(vx: float, vy: float, vz: float) -> float:
    return round(sqrt(vx**2 + vy**2 + vz**2), 2)

def pregunta_3(edad: int) -> str:
    if edad < 13:
        return "Menor"
    elif edad < 18:
        return "Adolescente"
    elif edad < 65:
        return "Adulto"
    else:
        return "Adulto Mayor"

def pregunta_4(peso: int, altura: float) -> str:
    imc = peso / (altura * altura)
    if imc < 18.5:
        return "Bajo peso"
    elif imc < 25:
        return "Normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidad"