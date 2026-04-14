from math import pi
import math

def pregunta_1(radio: float, angulo: float) -> float:
    longitud = radio * angulo * pi / 180
    return round(longitud, 2)
