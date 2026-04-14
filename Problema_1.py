"""Calcula la longitud del arco de una circunferencia dado el radio y el ángulo en grados sexagesimales.

Parámetros:
radio (float): El radio de la circunferencia.
angulo (float): El ángulo en grados sexagesimales.

Retorna:
float: La longitud del arco redondeada a dos decimales.
"""

import math

def calcular_longitud_arco(radio, angulo):
    L = radio * angulo * math.pi / 180
    return round(L, 2)

if __name__ == "__main__":
    radio = float(input("Introduce el radio: "))
    angulo = float(input("Introduce el ángulo en grados: "))
    resultado = calcular_longitud_arco(radio, angulo)
    print(f"La longitud del arco es: {resultado}")