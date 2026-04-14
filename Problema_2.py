import math

def pregunta_2(vx: float, vy: float, vz: float) -> float:
    """
    Parametros:
    vx (float): Es la coordenada en x
    vy (float): Es la coordenada en y
    vz (float): Es la coordenada en z
    Retorna:
    float : es el modulo
    """
    modulo = math.sqrt(vx**2 + vy**2 + vz**2)
    return round(modulo, 2)
