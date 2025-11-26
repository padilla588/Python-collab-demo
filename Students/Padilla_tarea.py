# =================================================================
# Nombre: Padilla
# Materia: Programación Orientada a Objetos / Estructura de Datos
# Tarea: Ejercicio de control de versiones con Git
# Descripción: Módulo que analiza un valor numérico ingresado por
#              el usuario para determinar su signo (Positivo/Negativo).
# =================================================================

def student_feature():
    """
    Función principal que gestiona la entrada de datos y la lógica
    de validación aritmética.
    """
    print("\n--- SISTEMA DE ANÁLISIS NUMÉRICO ---")
    
    try:
        # Solicitamos el valor y convertimos a float para mayor precisión
        entrada = input(">> Por favor, ingrese un valor numérico: ")
        numero = float(entrada)

        # Estructura condicional para evaluar el signo del número
        if numero > 0:
            print(f"Resultado: El número {numero} es POSITIVO (+).")
        elif numero < 0:
            print(f"Resultado: El número {numero} es NEGATIVO (-).")
        else:
            # Caso especial para el cero (elemento neutro)
            print("Resultado: El número es CERO (Neutro).")
            
    except ValueError:
        # Manejo de excepciones en caso de entrada no numérica
        print("Error [E01]: El dato ingresado no es un número válido.")
    
    print("-" * 40) # Separador estético final