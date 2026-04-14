def pregunta_3(edad: int) -> str:
    """
    Parametros:
    edad (int): Edad de la persona.
    Retorna:
    str: Clasificacion de la edad.
    """
    if edad < 13:
        return "Menor"
    elif edad < 18:
        return "Adolescente"
    elif edad < 65:
        return "Adulto"
    else:
        return "Adulto Mayor"
    