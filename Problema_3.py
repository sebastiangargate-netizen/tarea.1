def clasificar_edad(edad):
    """
    Clasifica la edad de una persona según los criterios dados.
    
    Parámetros:
    edad (int): La edad de la persona (0-120).
    
    Retorna:
    str: La categoría correspondiente.
    """
    if edad < 13:
        return "Menor"
    elif edad < 18:
        return "Adolescente"
    elif edad < 65:
        return "Adulto"
    else:
        return "Adulto Mayor"

if __name__ == "__main__":
    edad = int(input("Introduce la edad: "))
    categoria = clasificar_edad(edad)
    print(f"La categoría es: {categoria}")