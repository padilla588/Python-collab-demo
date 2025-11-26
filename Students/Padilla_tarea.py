def student_feature():
    """
    Pide un numero e imprime si es positivo, negativo o cero.
    """
    try:
        value = float(input("Ingresa un numero: "))
    except ValueError:
        print("Entrada invalida.")
        return

    if value > 0:
        print("Positivo.")
    elif value < 0:
        print("Negativo.")
    else:
        print("Cero.")